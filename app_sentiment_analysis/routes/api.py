from fastapi import APIRouter

from app_sentiment_analysis.model.model import SentimentAnalysisRequest
from app_sentiment_analysis.services.transformers import get_sentiment_analysis

router = APIRouter()

@router.post("/")
async def read_sentiment(mensage: SentimentAnalysisRequest):
    return get_sentiment_analysis(mensage.mensage)
    

