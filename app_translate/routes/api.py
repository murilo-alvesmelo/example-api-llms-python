from app_translate.model.model import TranslateRequest
from fastapi import APIRouter
from app_translate.services.translate_service import get_translation

router = APIRouter()

@router.post("/en-pt")
async def translate_en_pt(mensage: TranslateRequest):
    return get_translation(mensage.mensage)