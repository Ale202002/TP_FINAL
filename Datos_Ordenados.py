# Datos_Ordenados.py

import pandas as pd
from Carga_datos_encuestados import cargar_datos

def ordenar_datos(df):
    # Aquí colocas la lógica para ordenar los datos
    df_sorted = df.sort_values(by=['Estacion', 'Peso', 'Edad', 'Sexo'])
    
    print("-----Datos ordenados-----")
    print(df_sorted)
    
    return df_sorted

# Cargar datos usando la función del otro archivo
df_cargado = cargar_datos()

# Ordenar datos
df_ordenado = ordenar_datos(df_cargado)


