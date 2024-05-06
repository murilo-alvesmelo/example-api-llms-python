from pydantic import BaseModel, Field

class TranslateRequest(BaseModel):
    mensage: str 