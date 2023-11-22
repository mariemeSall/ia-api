import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from api.model import Wine
from csv import writer

attributes_name = ["fixed_acidity", 
    "volatile_acidity", 
    "citric_acid", 
    "residual_sugar",
    "cholrides",
    "free_sulfur_dioxide",
    "total_sulfur_dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol", 
    "quality"  ]

def modelCreation():
    
    data = pd.read_csv('Wines.csv')

    dataSet = data.drop(['quality', 'Id'], axis=1) 
    quality = data['quality']

    dataSet_train, dataSet_test, quality_train, quality_test = train_test_split(dataSet, quality, test_size=0.2, random_state=42)

    #Model avec 1127 arbres de decisions
    model = RandomForestRegressor(n_estimators=1127, random_state=42)

    #Entraine le model sur les data d'entrainement
    model.fit(dataSet_train, quality_train)

    # Use the forest's predict method on the test data
    predictions = model.predict(dataSet_test)
    rounded_predictions = [int(round(pred)) for pred in predictions] 

    mse = mean_squared_error(quality_test, rounded_predictions)
    print(f'Mean Squared Error on Test Data: {mse}')

    joblib.dump(model, './foret/wine_quality_model.joblib')

def predict(new_data):
    if not (os.path.exists('./foret/wine_quality_model.joblib')):
        modelCreation()

    # Charge le modèle à partir du fichier sauvegardé
    loaded_model = joblib.load('./foret/wine_quality_model.joblib')

    # DataFrame avec les valeurs saisies
    new_data_df = pd.DataFrame([new_data])
        


    # Prédiction de la qualité du vin saisi
    prediction = loaded_model.predict(new_data_df)[0]
    rounded_prediction = int(round(prediction))

    return rounded_prediction


def add_new_data(new_data: Wine):
    wine = [ ]
    for a in attributes_name :
        print(a)
        if not a.startswith('__'):
            b = getattr(new_data, a)
            print(b)
            wine.append(b)

    with open('Wines.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(wine)
        f_object.close()

    return True