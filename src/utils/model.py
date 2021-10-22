import tensorflow as tf
import time
import os

def create_model(loss_fn, optim, metrics, num_classes):
    LAYERS= [tf.keras.layers.Flatten(input_shape= [28,28], name='inputLayer'),
            tf.keras.layers.Dense(300, activation= 'relu', name='hiddenLayer_1'),
            tf.keras.layers.Dense(100, activation= 'relu', name='hiddenLayer_2'),
            tf.keras.layers.Dense(num_classes, activation= 'softmax', name='outputLlayer')
    ]
    model= tf.keras.models.Sequential(LAYERS)
    model.summary()
    model.compile(loss= loss_fn, optimizer= optim, metrics= metrics)
    return model #untrained

def get_unique_fileName(filename):
    unique_filename= time.strftime(f"%Y%m%d_%H%M%S_{filename}")
    return unique_filename


def save_model(model, model_name, model_dir):
    unique_filename= get_unique_fileName(model_name)
    print(unique_filename)
    path_to_model = os.path.join(model_dir, unique_filename)
    print(path_to_model)
    model.save(path_to_model)

