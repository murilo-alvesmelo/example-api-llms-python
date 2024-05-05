from pydantic import BaseModel, Field

class SentimentAnalysisRequest(BaseModel):
    mensage: str 