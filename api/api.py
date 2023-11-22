from fastapi import APIRouter
from api.model import *
from foret.foret import *


router = APIRouter()

@router.get("/api/predict")
async def show_characteristiques():
    return "get prediction characteristique"


@router.post("/api/predict")
async def do_predit(to_predict:Wine):
    return predict(to_predict)

@router.get("/api/model")
async def get_model_serialize():
    return joblib.load('./foret/wine_quality_model.joblib')

@router.get("/api/model/description")
async def get_model_infos():
    return "get model description"

@router.put("/api/model")
async def add_wine(wine: PredictedWine):
    return add_new_data(wine)

@router.post("/api/model/retrain")
async def retrain():
    return modelCreation()