from fastapi import APIRouter
from api.model import Wine


router = APIRouter()

@router.get("/api/predict")
async def show_characteristiques():
    return "get prediction characteristique"


@router.post("/api/predict")
async def do_predit(to_predict:Wine):
    return to_predict

@router.get("/api/model")
async def get_model_serialize():
    return "get model serialize"

@router.get("/api/model/description")
async def get_model_infos():
    return "get model description"

@router.put("/api/model")
async def add_wine(wine: Wine):
    return wine

@router.post("/api/model/retrain")
async def retrain():
    return "post retrain model"