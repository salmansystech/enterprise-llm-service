from fastapi import FastAPI, HTTPException
from app.schemas import InputSchema, OutputSchema
from app.utils import call_bedrock, mock_bedrock
import logging

# Setup logging
logging.basicConfig(filename="logs/app.log", level=logging.INFO)

app = FastAPI(title="Enterprise LLM Service")

@app.post("/analyze", response_model=OutputSchema)
def analyze(data: InputSchema):
    logging.info(f"Received input: {data.text}")
    try:
        # Replace with call_bedrock(data.text) if AWS available
        result = mock_bedrock(data.text)
        logging.info(f"Output: {result}")
        return result
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="LLM processing failed")
