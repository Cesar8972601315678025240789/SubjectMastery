import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os
import random

tr = 0



with open('nivel_actual.json', 'r') as archivo_json:
    datos = json.load(archivo_json)
tr = datos['nivel']
print(tr)

datos['nivel'] += 1
with open('nivel_actual.json', 'w') as archivo:
    json.dump(datos, archivo, indent=4)



def generar_numeros_aleatorios(cantidad):
    numeros_aleatorios = []
    for _ in range(cantidad):
        rango = random.randint(1, 5)
        if rango == 1:
            numero = random.randint(0, 9)
        elif rango == 2:
            numero = random.randint(10, 99)
        elif rango == 3:
            numero = random.randint(100, 999)
        elif rango == 4:
            numero = random.randint(1000, 9999)
        else:
            numero = random.randint(10000, 99999)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

# Llamamos a la función para generar 1,000 números aleatorios
mil_numeros_aleatorios = generar_numeros_aleatorios(1000)

def seleccionar_dos_aleatorios(numeros_aleatorios):
    if len(numeros_aleatorios) < 2:
        return None

    seleccionados = random.sample(numeros_aleatorios, 2)
    return seleccionados

with open("nivel.json", "r") as json_file:
    data = json.load(json_file)

operando1 = np.array([item["operando1"] for item in data])
operando2 = np.array([item["operando2"] for item in data])
nivelOperacion = np.array([item["nivelOperacion"] for item in data])

X = np.column_stack((operando1, operando2))
y = nivelOperacion

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

precision = accuracy_score(y_test, predicciones)
print("Precisión del modelo:", precision)

while True:
    dos_numeros_seleccionados = seleccionar_dos_aleatorios(mil_numeros_aleatorios)

    entrada_nueva = np.array([[dos_numeros_seleccionados[0], dos_numeros_seleccionados[1]]])
    prediccion = modelo.predict(entrada_nueva)
    print("La predicción es:", prediccion[0])
    
    if prediccion[0] == tr:
        print(dos_numeros_seleccionados)
        # Save dos_numeros_seleccionados to operandos_actuales.json
        with open("operandos_actuales.json", "w") as json_file:
            json.dump({"operando1": dos_numeros_seleccionados[0], "operando2": dos_numeros_seleccionados[1]}, json_file)
        
        break