import tensorflow as tf

def get_data(val_size):
    mnist= tf.keras.datasets.mnist
    print('load data...')
    (X_train_full, y_train_full), (X_test, y_test) = mnist.load_data()
    print('complete!')
    #create validation dataset
    X_val, X_train = X_train_full[:val_size] / 255. , X_train_full[val_size:]/255.
    y_val, y_train = y_train_full[:val_size] / 255. , y_train_full[val_size:]/255.
    
    X_test= X_test/255.
    print(len(X_test))
    print(y_val)
    return (X_train, y_train), (X_val, y_val), (X_test, y_test)