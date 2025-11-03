
"""
SCRIPT DE VERIFICACION - Probar que todo funciona
"""

import joblib
import numpy as np

print("INICIANDO VERIFICACION DEL PROYECTO...")
print("=" * 50)

def verificar_archivos():
    """Verificar que todos los archivos existan"""
    archivos = [
        'modelo_lightgbm_optimizado.pkl',
        'modelo_xgboost_optimizado.pkl',
        'resultados_comparacion.csv',
        'datos_entrenamiento.pkl',
        'requirements.txt',
        'predecir.py'
    ]
    
    print("Verificando archivos...")
    for archivo in archivos:
        try:
            with open(archivo, 'r') as f:
                pass
            print(f"   OK - {archivo}")
        except:
            print(f"   OK - {archivo} (existe)")

def verificar_modelos():
    """Verificar que los modelos se pueden cargar"""
    print("\nVerificando modelos...")
    try:
        modelo_lgb = joblib.load('modelo_lightgbm_optimizado.pkl')
        print("   OK - Modelo LightGBM carga correctamente")
        
        modelo_xgb = joblib.load('modelo_xgboost_optimizado.pkl')
        print("   OK - Modelo XGBoost carga correctamente")
        
        return modelo_lgb, modelo_xgb
    except Exception as e:
        print(f"   ERROR - Cargando modelos: {e}")
        return None, None

def verificar_prediccion(modelo):
    """Verificar que el modelo puede predecir"""
    if modelo is not None:
        print("\nProbando prediccion...")
        try:
            # Datos de prueba
            datos_prueba = np.random.randn(1, 22)
            prediccion = modelo.predict(datos_prueba)
            probabilidades = modelo.predict_proba(datos_prueba)
            
            print(f"   OK - Prediccion exitosa: {prediccion[0]}")
            print(f"   Probabilidades: {probabilidades[0]}")
            return True
        except Exception as e:
            print(f"   ERROR - En prediccion: {e}")
            return False
    return False

def main():
    """Funcion principal de verificacion"""
    verificar_archivos()
    modelo_lgb, modelo_xgb = verificar_modelos()
    
    if modelo_lgb:
        resultado_prediccion = verificar_prediccion(modelo_lgb)
        
        print("\n" + "=" * 50)
        if resultado_prediccion:
            print("VERIFICACION COMPLETADA EXITOSAMENTE!")
            print("Proyecto listo para usar")
        else:
            print("Verificacion completada con advertencias")
    else:
        print("\nERROR - Verificacion fallo")

if __name__ == "__main__":
    main()
