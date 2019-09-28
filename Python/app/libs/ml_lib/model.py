from numpy import array
from keras.models import load_model
import numpy as np



class ModelLoader:
    # model = None

    # def __init__(self):        
    #     if not ModelLoader.model:
    #         ModelLoader.model = load_model('/home/anton/VSCodeProjects/hackathone/Python/app/libs/data/model7.h5')
    #         ModelLoader.model._make_predict_function()
    #         ModelLoader.model.predict(np.ones((1, 26, 34, 1)))

    @staticmethod
    def predict(data: array) -> float:
        model = load_model('/home/anton/VSCodeProjects/hackathone/Python/app/libs/data/model7.h5')
        return model.predict(data)
