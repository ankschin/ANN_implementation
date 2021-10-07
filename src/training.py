import imp
from os import defpath
from typing import DefaultDict
from utils.common import read_config
from utils.data_mgmt import get_data
import argparse
from pathlib import Path



def training(config_path):
    config= read_config(config_path)
    #print(config)

    val_dataSize= config['params']['validation_size']
    (X_train, y_train), (X_val, y_val), (X_test, y_test)= get_data(val_size=val_dataSize)



if __name__=="__main__":
    args= argparse.ArgumentParser()

    #get current file's path
    yaml_path = Path(__file__).resolve()  # resolve to get rid of any symlinks
    
    #get current file's parent(src) -> parent(where config yaml resides) 
    config_path = yaml_path.parent.parent / 'config.yaml'
    args.add_argument("--config", "-c", default=config_path)
    parsed_args,_= args.parse_known_args()
    training(config_path=parsed_args.config)
