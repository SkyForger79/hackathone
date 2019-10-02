from numpy import array
from keras.models import load_model
import numpy as np


class ModelLoader:

    @staticmethod
    def predict(data: array) -> float:
        model = load_model('/home/anton/VSCodeProjects/hackathone/Python/app/libs/data/model7.h5')
        return model.predict(data)
