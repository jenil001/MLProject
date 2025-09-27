import os
import pandas as pd
import numpy as np
import sys
import pickle
import dill

from src.logger import logging
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as f:
            dill.dump(obj, f)
            logging.info(f"Object saved at: {file_path}")
    except Exception as e:
        logging.error("Error in save_object")
        raise CustomException(e, sys)