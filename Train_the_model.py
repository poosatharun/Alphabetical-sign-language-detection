import os
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
#from tensorflow.keras import layers
#from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set up the data generator with image augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Load the training data from a directory
train_data = train_datagen.flow_from_directory('Data',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Save the class labels to a text file
with open('flabels.txt', 'w') as f:
    for label in train_data.class_indices:
        f.write(f"{label}\n")

# Set up the base model (MobileNetV2 in this example)
base_model = keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

# Freeze the base model's layers
for layer in base_model.layers:
    layer.trainable = False

# Add a custom head to the model
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(train_data.num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_data, epochs=10)

# Save the model
model.save('fmodel.h5')