import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
import random


with open('/Users/administrador/downloads/datos.json', 'r') as archivo_json:
    datos = json.load(archivo_json)
    nivel_actual = datos['nivel']
    print(nivel_actual)
    os.remove('/Users/administrador/downloads/datos.json')
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

mil_numeros_aleatorios = generar_numeros_aleatorios(1000)

def seleccionar_uno_aleatorio(numeros_aleatorios):
    seleccionados = random.sample(numeros_aleatorios, 1)
    return seleccionados


#---------

with open('nivel.json', 'r') as archivo:
    datos_json = json.load(archivo)

operando1 = [entrada["operando1"] for entrada in datos_json]
nivelOperacion = [entrada["nivelOperacion"] - 1 for entrada in datos_json]


operando1 = np.array(operando1)
nivelOperacion = np.array(nivelOperacion)


modelo = keras.Sequential([
    keras.layers.Dense(units=64, activation='relu', input_shape=(1,)),
    keras.layers.Dense(units=5, activation='softmax')
])


modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


modelo.fit(operando1, nivelOperacion, epochs=1000)


def clasificar_numero(numero):
    numero = np.array([numero])
    prediccion = modelo.predict(numero)
    clase_predicha = np.argmax(prediccion) + 1  
    return clase_predicha


while True:
    numero_a_clasificar1 = seleccionar_uno_aleatorio(mil_numeros_aleatorios)
    clasificacion = clasificar_numero(numero_a_clasificar1)
    print(f"El número {numero_a_clasificar1} se clasifica como {clasificacion}")
    
    if clasificacion == nivel_actual:
        while True:
            numero_a_clasificar2 = seleccionar_uno_aleatorio(mil_numeros_aleatorios)
            clasificacion = clasificar_numero(numero_a_clasificar2)
            print(f"El número {numero_a_clasificar2} se clasifica como {clasificacion}")
    
            if clasificacion == nivel_actual:
                # Save dos_numeros_seleccionados to operandos_actuales.json
                with open("operandos_actuales.json", "w") as json_file:
                    json.dump({"operando1": numero_a_clasificar1, "operando2":numero_a_clasificar2,"nivel_actual": nivel_actual}, json_file)
        
                break
        break




