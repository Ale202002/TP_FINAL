# Carga_datos_encuestados.py

import pandas as pd

def cargar_datos():

    pesos = [80.5, 65.2]
    edades = [30, 25]
    sexos = ['M', 'F']
    estaciones = ['Retiro', 'Constitucion']

    datos = {"Peso": pesos, "Edad": edades, "Sexo": sexos, "Estacion": estaciones}
    df = pd.DataFrame(datos)
    
    print("-----Datos cargados-----")
    print(df)

    return df

#Llamamos a la función solo si este script es ejecutado directamente

if __name__ == "__main__":
    cargar_datos()






