from marshmallow import ValidationError
from app.libs.ml_lib.model import ModelLoader
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image  
import os
from datetime import datetime
from keras.models import load_model
from keras import backend as cl
import cv2
from PIL import Image
import config
from time import sleep


eye_cascade = cv2.CascadeClassifier('/home/pavel/PycharmProjects/hackathone/Python/app/libs/data/opencv_face.xml')


def image_preprocessing(image):
    img_eye = Image.fromarray(image, 'RGB')
    img_eye = img_eye.resize((34, 26), Image.ANTIALIAS).convert('L')
    return np.expand_dims(np.array(img_eye), axis=2) / 255.


def detect_eyes(image):
    gray_frame = np.array(cv2.cvtColor(np.float32(image), cv2.COLOR_BGR2GRAY), dtype='uint8')
    eyes = eye_cascade.detectMultiScale(gray_frame, 1.3, 50)
    for (x, y, w, h) in eyes:
        yield image_preprocessing(image[y:y + h, x:x + w])


def check_fatigue(file):
    filename = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
    file_path = os.path.join(config.UPLOAD_FOLDER, filename + '.jpeg')
    file.save(file_path)
    img = cv2.imread(file_path)
    arr_eye = np.array([i for i in detect_eyes(img)])
    # model = load_model('./app/libs/data/model7.h5')
    # model._make_predict_function()
    predict = [float(i) for i in ModelLoader().predict(arr_eye)]
    # predict = [float(i) for i in model.predict(arr_eye)]
    cl.clear_session()
    return {'predict ': list(predict)}
