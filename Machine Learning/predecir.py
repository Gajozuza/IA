
"""
SCRIPT DE PREDICCION - Modelo LightGBM
Proyecto: Comparacion XGBoost vs LightGBM
"""

import joblib
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class PredictorLightGBM:
    def __init__(self, model_path='modelo_lightgbm_optimizado.pkl'):
        """Inicializar el predictor cargando el modelo"""
        self.model = joblib.load(model_path)
        print("OK - Modelo LightGBM cargado exitosamente")
        
    def predecir(self, datos):
        """
        Realizar predicciones con nuevos datos
        
        Parameters:
        datos: array-like, DataFrame o lista con 22 caracteristicas
        
        Returns:
        prediccion: clase predicha (0 o 1)
        probabilidades: probabilidades para cada clase
        """
        # Convertir a formato correcto (2D array)
        if isinstance(datos, list):
            datos = np.array(datos).reshape(1, -1)  # ← CORRECCIÓN AQUÍ
        elif isinstance(datos, pd.DataFrame):
            datos = datos.values
        elif isinstance(datos, np.ndarray) and datos.ndim == 1:
            datos = datos.reshape(1, -1)  # ← CORRECCIÓN AQUÍ
            
        # Verificar que tenga 22 características
        if datos.shape[1] != 22:
            print(f"ADVERTENCIA: Se esperaban 22 características, se recibieron {datos.shape[1]}")
            
        # Realizar prediccion
        prediccion = self.model.predict(datos)
        probabilidades = self.model.predict_proba(datos)
        
        print(f"Prediccion: {prediccion[0]}")
        print(f"Probabilidades: Clase 0: {probabilidades[0][0]:.3f}, Clase 1: {probabilidades[0][1]:.3f}")
        
        return prediccion[0], probabilidades[0]

def main():
    """Funcion principal con ejemplo de uso"""
    # Inicializar predictor
    predictor = PredictorLightGBM()
    
    # EJEMPLO: Crear datos de prueba (CORREGIDO)
    print("\nEJEMPLO DE PREDICCION:")
    datos_ejemplo = np.random.randn(22)  # 22 características aleatorias
    
    # Realizar prediccion
    try:
        prediccion, probs = predictor.predecir(datos_ejemplo)
        
        print(f"Interpretacion: {'Clase 0' if prediccion == 0 else 'Clase 1'}")
        print(f"Confianza: {max(probs):.3f}")
        
    except Exception as e:
        print(f"ERROR en prediccion: {e}")
        print("Intentando con formato alternativo...")
        
        # Formato alternativo seguro
        datos_ejemplo_2d = np.random.randn(1, 22)  # Ya en 2D
        prediccion, probs = predictor.predecir(datos_ejemplo_2d)
        print(f"Prediccion alternativa: {prediccion}")
        print(f"Probabilidades: {probs}")

if __name__ == "__main__":
    main()
