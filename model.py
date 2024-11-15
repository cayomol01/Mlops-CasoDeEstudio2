# pipeline.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib  # Para guardar el modelo

def load_data(file_path):
    """Carga el dataset."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Procesa los datos: limpia y prepara para el modelo."""
    df = df.fillna(df.mean(numeric_only=True))
    df['Score'] = df['km4week']*df['sp4week']
    df = df[~df['Wall21'].str.contains('-')]  # Filtrar valores no deseados
    return df

def train_model(df):
    """Entrena un modelo de regresión."""
    X = df[['km4week', 'sp4week', 'Wall21', 'Score']].values
    y = df['MarathonTime'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    return model

def save_model(model, file_path):
    """Guarda el modelo entrenado."""
    joblib.dump(model, file_path)

def load_model(file_path):
    try:
        model = joblib.load(file_path)
        print(f"Modelo cargado desde {file_path}")
        return model
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe.")
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")


def main():
    # Ruta al archivo de datos
    data_file = "MarathonData.csv"
    model_file = "Models/modelV1.pkl"

    # Pipeline de procesamiento
    df = load_data(data_file)
    df = preprocess_data(df)
    model = train_model(df)
    
    save_model(model, model_file)
    print(f"Modelo guardado en {model_file}")

if __name__ == "__main__":
    main()
