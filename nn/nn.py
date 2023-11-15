import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

def get_data(file:str):

    df = pd.read_csv(file)

    dataset = df.values

    #Input variable
    X = dataset[:,0:12]

    #Output variable
    Y = dataset[:,12]


    min_max_scaler = preprocessing.MinMaxScaler()
    X_scale = min_max_scaler.fit_transform(X)

    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
    return X_train, X_val, X_test, Y_train, Y_val, Y_test

#print( get_data('Wines.csv'))

X_train, X_val, X_test, Y_train, Y_val, Y_test = get_data('Wines.csv')
model = Sequential([
    Dense(36, activation='relu', input_shape=(12,)),
    Dense(36, activation='relu'),
    Dense(1, activation='sigmoid'),
])

model.compile(optimizer='sgd',
              loss='crossentropy',
              metrics=['accuracy'])

hist = model.fit(X_train, Y_train,
          batch_size=32, epochs=100,
          validation_data=(X_val, Y_val))

