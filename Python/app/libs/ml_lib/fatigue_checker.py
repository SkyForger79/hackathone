from marshmallow import ValidationError
from Python.app.libs.ml_lib.model import ModelLoader
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image  
import os
from datetime import datetime
from keras.models import load_model
from keras import backend as cl
import cv2
from PIL import Image
import Python.config as config
from time import sleep
from keras import backend as K

face_cascade = cv2.CascadeClassifier('/home/anton/VSCodeProjects/hackathone/Python/app/libs/data/opencv_face2.xml')
eye_cascade = cv2.CascadeClassifier('/home/anton/VSCodeProjects/hackathone/Python/app/libs/data/opencv_face.xml')


def image_preprocessing(image):
    img_eye = Image.fromarray(image)
    img_eye = img_eye.resize((34, 26), Image.ANTIALIAS).convert('L')
    return np.expand_dims(np.array(img_eye), axis=2) / 255.


def detect_eyes(image):
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    print(len(faces))
    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 7)
        print(len(eyes))
        for (ex, ey, ew, eh) in eyes:
            yield image_preprocessing(roi_gray[ey:ey + eh, ex:ex + ew])


def check_fatigue(file):
    filename = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
    file_path = os.path.join(config.UPLOAD_FOLDER, filename + '.jpeg')
    file.save(file_path)
    img = cv2.imread(file_path)
    arr_eye = np.array([i for i in detect_eyes(img)])
    # model = load_model('./app/libs/data/model7.h5')
    # model._make_predict_function()
    if len(arr_eye) > 0:
        K.clear_session()
        predict = [float(i) for i in ModelLoader().predict(arr_eye)]
        K.clear_session()
        return {'predict ': list(predict)}
    else:
        return {'predict ': [-1, -1]}
