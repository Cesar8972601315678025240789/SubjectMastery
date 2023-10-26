import numpy as np
from sklearn.neural_network import MLPRegressor
import json


with open("nota.json", "r") as json_file:
    data = json.load(json_file)


X = np.array([sample["nivel"] for sample in data])
y = np.array([sample["nota"] for sample in data])


model = MLPRegressor(hidden_layer_sizes=(2), activation='identity', max_iter=8000)
model.fit(X.reshape(-1, 1), y)


nivel_prediccion = 5  
X_test = np.array([nivel_prediccion])
prediction = model.predict(X_test.reshape(-1, 1))
print(f"Predicción para nivel {nivel_prediccion}: {prediction[0]}")
