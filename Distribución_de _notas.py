import pandas as pd
import matplotlib.pyplot as plt

def grafico_notas_alumno(notas_dict, nombre_alumno):
    # Verifica si la entrada es un diccionario
    if not isinstance(notas_dict, dict):
        raise ValueError("Se espera un diccionario como entrada.")

    # Verifica si el nombre del alumno está en el diccionario
    if nombre_alumno not in notas_dict:
        raise ValueError(f"El alumno '{nombre_alumno}' no se encuentra en el diccionario de notas.")

    # Extrae las notas del alumno especificado
    notas_alumno = notas_dict[nombre_alumno]

    # Crea el gráfico de barras
    plt.bar(notas_alumno.keys(), notas_alumno.values(), color='skyblue')

    # Agrega título y etiquetas al gráfico
    plt.title(f'Notas de {nombre_alumno}')
    plt.xlabel('Asignaturas')
    plt.ylabel('Notas')

    # Muestra el gráfico
    plt.show()

# Ejemplo de uso
notas_curso = {
    'Juan': {'Matemáticas': 8, 'Historia': 7, 'Ciencias': 9},
    'Ana': {'Matemáticas': 9, 'Historia': 8, 'Ciencias': 7},
    'Carlos': {'Matemáticas': 7, 'Historia': 6, 'Ciencias': 8}
}

nombre_alumno_ejemplo = 'Juan'
grafico_notas_alumno(notas_curso, nombre_alumno_ejemplo)


def grafico_distribucion_notas(notas_serie):
    # Verifica si la entrada es una serie de Pandas
    if not isinstance(notas_serie, pd.Series):
        raise ValueError("Se espera una serie de Pandas como entrada.")

    # Cuenta la frecuencia de cada nota
    frecuencia_notas = notas_serie.value_counts().sort_index()

    # Crea el gráfico de barras
    plt.bar(frecuencia_notas.index, frecuencia_notas.values, color='skyblue')

    # Agrega título y etiquetas al gráfico
    plt.title('Distribución de notas')
    plt.xlabel('Notas')
    plt.ylabel('Frecuencia')

    # Muestra el gráfico
    plt.show()

# Ejemplo de uso
notas_alumnos = pd.Series([5, 8, 9, 4, 6, 10, 5, 8, 6, 6, 9])
grafico_distribucion_notas(notas_alumnos)

