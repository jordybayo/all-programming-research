import tensorflow as tf
from dataset import *

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', imput_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Fluttern the results to feed into a DNN
    tf.keras.layers.Flatten(),
    tf.keras.layers.dropout(0.5),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu')
    tf.keras.layers.Dense(3, activation='softmax')
])

history = model.ft_generator(train_generator, epochs=25,
validation_data = validation_generator.,
verbose = 1)