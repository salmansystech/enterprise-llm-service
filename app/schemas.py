# app/schemas.py

from pydantic import BaseModel

class InputSchema(BaseModel):
    text: str

class OutputSchema(BaseModel):
    risk_score: float
    reasoning: str
    confidence: float
