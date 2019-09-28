import config
import os
from datetime import datetime
from app.libs.insert_screen import insert_to_alert_history


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS


def check_eyes(file, result_check):
    filename = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
    left_eye = result_check['predict '][0]
    right_eye = result_check['predict '][1]
    insert_to_alert_history(filename + '.jpeg', left_eye, right_eye)
    print(str(result_check))
    if left_eye < 0.2 or right_eye < 0.2:
        return {"head": "Вы устали!", "hody": "Рекомендуется устроить небольшой перерыв", "img": filename, "id": 3,
                "level": "danger"}
    return None