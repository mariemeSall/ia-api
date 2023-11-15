import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib


def modelCreation():
    
    data = pd.read_csv('../Wines.csv')

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

print(predict({
    'fixed acidity': 10.7,
    'volatile acidity': 0.35,
    'citric acid': 0.53,
    'residual sugar': 2.6,
    'chlorides': 0.07,
    'free sulfur dioxide': 5.0,
    'total sulfur dioxide': 7.0,
    'density': 0.9972,
    'pH': 3.15,
    'sulphates': 0.65,
    'alcohol': 11.0
}))