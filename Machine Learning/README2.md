
# Proyecto: Comparacion XGBoost vs LightGBM

## Resultados

| Modelo | Accuracy Test | CV Mean | Estabilidad |
|--------|---------------|---------|-------------|
| **LightGBM** | 0.9800 | 0.9800 | 0.0108 |
| XGBoost | 0.9800 | 0.9738 | 0.0133 |

## Modelo Ganador: LightGBM

**Razones:**
- Mayor consistencia en validacion cruzada
- Menor variabilidad entre folds
- Mismo rendimiento en test

## Archivos del Proyecto

- modelo_lightgbm_optimizado.pkl - Modelo entrenado
- predecir.py - Script para hacer predicciones
- probar_modelo.py - Verificar que todo funciona
- requirements.txt - Dependencias necesarias

## Uso Rapido
Verificar que todo funciona
python probar_modelo.py

Hacer una prediccion
python predecir.py

text

Proyecto listo para produccion!
