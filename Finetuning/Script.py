from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224,224,3))
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(5, activation='softmax')(x) # ejemplo: 5 clases
model = Model(inputs=base_model.input, outputs=predictions)
# Congelar capas base
for layer in base_model.layers:
 layer.trainable = False
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# Ejemplo con generador de imágenes (debe adaptarse dataset)
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_gen = datagen.flow_from_directory('flower_photos', target_size=(224,224),
batch_size=32, class_mode='categorical', subset='training')

val_gen = datagen.flow_from_directory('flower_photos', target_size=(224,224),
batch_size=32, class_mode='categorical', subset='validation')
model.fit(train_gen, validation_data=val_gen, epochs=5)
# Para fine-tuning, desbloquear algunas capas y reentrenar con menor tasa de aprendizaje
# 1. Descongelar las últimas capas del modelo base
# Se recomienda descongelar solo las últimas capas, ya que las primeras aprenden
# características muy generales (bordes, colores) y no deben modificarse.
base_model.trainable = True

# Congelar todas las capas excepto las últimas ~20 capas (ejemplo)
# Usa len(base_model.layers) para saber el total de capas. MobileNetV2 tiene ~155 capas.
# Aquí descongelamos las capas 100 en adelante, manteniendo las primeras congeladas.
fine_tune_at = 100

for layer in base_model.layers[:fine_tune_at]:
    layer.trainable = False

# 2. Recompilar el modelo con una TASA DE APRENDIZAJE MUY BAJA (clave del Fine-Tuning)
from tensorflow.keras.optimizers import Adam
model.compile(
    optimizer=Adam(learning_rate=0.00001), # La tasa es 100 veces menor que 'adam' por defecto
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 3. Reentrenar el modelo (Fine-Tuning)
print("\nIniciando Fine-Tuning de las últimas capas...")
fine_tune_epochs = 5
total_epochs = 5 + fine_tune_epochs

model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=total_epochs,
    initial_epoch=5 # Continuar el entrenamiento desde la epoch 5
)