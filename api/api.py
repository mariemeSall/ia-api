import json
from fastapi import APIRouter
from api.model import *
from foret.foret import *


router = APIRouter()

@router.get("/api/predict")
async def show_characteristiques():
    return "get prediction characteristique"


@router.post("/api/predict")
async def do_predit(to_predict:Wine):
    wine = {
        "fixed_acidity": to_predict.fixed_acidity,    
    "volatile_acidity": to_predict.volatile_acidity,    
    "citric_acid": to_predict.citric_acid,    
    "residual_sugar": to_predict.residual_sugar,
    "chlorides": to_predict.chlorides,   
    "free_sulfur_dioxide": to_predict.free_sulfur_dioxide,    
    "total_sulfur_dioxide": to_predict.total_sulfur_dioxide,    
    "density": to_predict.density,
    "pH": to_predict.pH,   
    "sulphates": to_predict.sulphates,    
    "alcohol": to_predict.alcohol
    }
    return predict(wine)

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