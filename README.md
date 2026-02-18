# Enterprise LLM Service

A FastAPI-based API that sends text input to a Large Language Model (LLM) and returns structured JSON output. Can use **AWS Bedrock** or a **mock LLM** for local testing.

## Features

- `/analyze` endpoint accepts text input
- Returns structured JSON with fields:
  - `risk_score`
  - `reasoning`
  - `confidence`
- Input validation with **Pydantic**
- Logging of requests and outputs
- Mock mode for testing without AWS
- Ready for Docker and CI/CD

## Installation

Clone the repository:

```bash
git clone https://github.com/salmansystech/enterprise-llm-service.git
cd enterprise-llm-service

Create and activate a virtual environment:

python -m venv .venv
& .\.venv\Scripts\Activate.ps1


Install dependencies:

pip install -r requirements.txt

Usage

Run the API server:

uvicorn app.main:app --reload


Open http://127.0.0.1:8000/docs
 to test the endpoint.

Example Input
{
  "text": "Evaluate the risk of this customer transaction"
}

Example Output
{
  "risk_score": 0.5,
  "reasoning": "Mocked reasoning for: Evaluate the risk of this customer transaction",
  "confidence": 0.9
}

Configuration

Edit app/config.py:

AWS_KEY = "YOUR_ACCESS_KEY_ID"
AWS_SECRET = "YOUR_SECRET_ACCESS_KEY"
AWS_REGION = "us-east-1"

# Use mock responses if AWS Bedrock is not accessible
USE_MOCK = True


USE_MOCK = True → mock LLM for local testing

USE_MOCK = False → call AWS Bedrock

Logging

Requests and outputs are logged in logs/app.log.