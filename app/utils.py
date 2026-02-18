# app/utils.py

import boto3
import json
from app.config import AWS_KEY, AWS_SECRET, AWS_REGION, USE_MOCK

def call_bedrock(prompt: str, model_id="amazon.titan-tg-alpha"):
    """Send a prompt to AWS Bedrock and return the response"""
    if USE_MOCK:
        return mock_bedrock(prompt)

    session = boto3.Session(
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET,
        region_name=AWS_REGION
    )
    bedrock = session.client("bedrock")

    response = bedrock.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({"inputText": prompt})
    )
    # Decode response from bytes to string
    result = response['body'].read().decode("utf-8")
    # Here you can process result into structured JSON if needed
    return json.loads(result)

def mock_bedrock(text: str):
    """Return a fake structured response for testing"""
    return {
        "risk_score": 0.5,
        "reasoning": f"Mocked reasoning for: {text}",
        "confidence": 0.9
    }
