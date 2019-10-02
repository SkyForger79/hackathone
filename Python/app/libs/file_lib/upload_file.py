import Python.config
from Python import config
import os
from datetime import datetime
from Python.app.libs.insert_screen import insert_to_alert_history, get_fatigue_signal


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS


def save_data(result_check):
    filename = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
    eye = max(result_check['predict '])
    insert_to_alert_history(filename + '.jpeg', eye)
    get_fatigue_signal()
    # print(str(result_check))
    # if left_eye < 0.2 or right_eye < 0.2:
    #     return {"head": "Вы устали!", "hody": "Рекомендуется устроить небольшой перерыв", "img": filename, "id": 3,
    #             "level": "danger"}
    # return None

