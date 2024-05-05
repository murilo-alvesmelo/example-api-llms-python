
from fastapi import FastAPI
from app_sentiment_analysis.routes.api import router as analise_sentimental_router
app = FastAPI()

app.include_router(analise_sentimental_router, prefix="/analise_sentimental_router")
