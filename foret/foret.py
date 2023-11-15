import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

data = pd.read_csv('../Wines.csv')

# Séparation des données en caractéristiques (X) et variable cible (y)
dataSet = data.drop(['quality', 'Id'], axis=1)  # Excluez 'Id' car il semble être un identifiant unique
quality = data['quality']

dataSet_train, dataSet_test, quality_train, quality_test = train_test_split(dataSet, quality, test_size=0.2, random_state=42)


print('Training dataSet Shape:', dataSet_train.shape)
print('Training dataSet_test Shape:', dataSet_test.shape)
print('Testing quality_train Shape:', quality_train.shape)
print('Testing quality_test Shape:', quality_test.shape)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(dataSet_train, quality_train)
