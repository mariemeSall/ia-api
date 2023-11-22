from pydantic import BaseModel


class Wine(BaseModel):
    fixed_acidity: float    
    volatile_acidity:float    
    citric_acid: float    
    residual_sugar: float
    cholrides: float    
    free_sulfur_dioxide: float    
    total_sulfur_dioxide: float    
    density: float
    pH: float    
    sulphates: float    
    alcohol: float    

class PredictedWine(BaseModel):
    fixed_acidity: float    
    volatile_acidity:float    
    citric_acid: float    
    residual_sugar: float
    cholrides: float    
    free_sulfur_dioxide: float    
    total_sulfur_dioxide: float    
    density: float
    pH: float    
    sulphates: float    
    alcohol: float 
    quality: int
