
import pandas as pd

def leer_datos(ruta=r'C:\Users\i.monsalve.rodilla\trial_clase\data\datos_mock.csv'):
    """Lee el archivo CSV y devuelve un DataFrame."""
    return pd.read_csv(ruta, sep=";")

def calcular_media(df):
    """Calcula la media de la columna 'valor'."""
    return df['valor'].mean()

if __name__ == '__main__':
    df = leer_datos()
    media = calcular_media(df)
    print(f"La media de la columna 'valor' es: {media}")

    print("End")
