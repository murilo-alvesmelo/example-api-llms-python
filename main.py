
from fastapi import FastAPI

from app_sentiment_analysis.routes.api import router as analise_sentimental_router
from app_translate.routes.api import router as translate_router

app = FastAPI()

app.include_router(analise_sentimental_router, prefix="/analise_sentimental_router")
app.include_router(translate_router, prefix="/translate")
