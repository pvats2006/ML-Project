import os
import sys
import dill


from src.exception import CustomException


import numpy as np
import pandas as pd




def save_object(file_path, obj):
    try:
        # directory path nikal rahe hain
        dir_path = os.path.dirname(file_path)

        # agar directory exist nahi karti to create karo
        os.makedirs(dir_path, exist_ok=True)

        # object ko binary mode me save kar rahe hain
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)