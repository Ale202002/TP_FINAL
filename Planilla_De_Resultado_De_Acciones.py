import pandas as pd

def resumen_cotizaciones(fichero):
    try:
        df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
        resumen = pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])
        return resumen
    except Exception as e:
        print(f"Error: {e}")

# Llamada a la función
resultado = resumen_cotizaciones('cotizacion.csv')

# Imprimir el resultado si no hay errores
if resultado is not None:
    print(resultado)
