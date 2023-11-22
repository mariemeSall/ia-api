import json
from pydantic import BaseModel


class Wine(BaseModel):
    fixed_acidity: float    
    volatile_acidity:float    
    citric_acid: float    
    residual_sugar: float
    chlorides: float    
    free_sulfur_dioxide: float    
    total_sulfur_dioxide: float    
    density: float
    pH: float    
    sulphates: float    
    alcohol: float  
     
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
 

class PredictedWine(BaseModel):
    fixed_acidity: float    
    volatile_acidity:float    
    citric_acid: float    
    residual_sugar: float
    chlorides: float    
    free_sulfur_dioxide: float    
    total_sulfur_dioxide: float    
    density: float
    pH: float    
    sulphates: float    
    alcohol: float 
    quality: int
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

