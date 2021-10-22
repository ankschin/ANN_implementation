import os
from os import defpath
from typing import DefaultDict
from utils.model import create_model, save_model
from utils.common import read_config
from utils.data_mgmt import get_data
import argparse
from pathlib import Path



def training(config_path):
    config= read_config(config_path)
    #print(config)
    val_dataSize= config['params']['validation_size']
    (X_train, y_train), (X_val, y_val), (X_test, y_test)= get_data(val_size=val_dataSize)

    loss_fun= config['params']['loss_function']
    optimizer= config['params']['optimizer']
    metrics= config['params']['metric']
    n_class= config['params']['n_classes']
    epochs= config['params']['epochs']

    model= create_model(loss_fun, optimizer, metrics, n_class)

    valid_set= (X_val, y_val)
    
    hist= model.fit(X_train, y_train, epochs= epochs, validation_data= valid_set)

    artifacts_dir= config['artifacts']['artifacts_dir']
    model_dir= config['artifacts']['model_dir']
    model_name= config['artifacts']['model_name']

    model_dir_path= os.path.join(artifacts_dir, model_dir)
    os.makedirs(model_dir_path, exist_ok=True)

    save_model(model, model_name, model_dir_path)


if __name__=="__main__":
    args= argparse.ArgumentParser()

    #get current file's path
    yaml_path = Path(__file__).resolve()  # resolve to get rid of any symlinks
    
    #get current file's parent(src) -> parent(where config yaml resides) 
    config_path = yaml_path.parent.parent / 'config.yaml'
    args.add_argument("--config", "-c", default=config_path)
    parsed_args,_= args.parse_known_args()
    training(config_path=parsed_args.config)