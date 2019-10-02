from marshmallow import ValidationError
from flask import Blueprint, request, jsonify, send_from_directory, Response

from Python.app.libs.file_lib.upload_file import allowed_file, save_data
from Python.app.libs.ml_lib.fatigue_checker import check_fatigue
from Python.app.libs.sql_lib.insert_signal import insert_to_alert_history, insert_alert_to_database
from Python.app.libs.sql_lib.d_get_signals import get_last_signals, get_all_signals


import json
import Python.config as config
import json
import glob
import os

blueprints_v1 = Blueprint(__name__, 'blueprints_v1', url_prefix='/v1')


@blueprints_v1.route('get_status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})


# region ml
@blueprints_v1.route('/ml', methods=['GET', 'POST'])
def ml():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            result = check_fatigue(file)
            # upload = check_eyes(file)
            # answer = list()
            # answer.append(upload)
            # answer.append(result)
            return result
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''
# endregion


# region arduino
@blueprints_v1.route('/set_stat', methods=['GET'])
def set_stat():
    light = request.args.get('Light'),
    micro = request.args.get('microphoneValue'),
    sonar = request.args.get('Sonar'),
    humidity = request.args.get('Humidity'),
    temperature = request.args.get('temperature')


    if int(light[0]) > config.max_light:
        insert_to_alert_history(light=request.args.get('Light'))
    if int(micro[0]) > config.max_micro:
        insert_to_alert_history(micro=request.args.get('microphoneValue'))
    if int(sonar[0]) < config.min_sonar:
        insert_to_alert_history(sonar=request.args.get('Sonar'))
    if float(humidity[0]) > config.max_humidity:
        insert_to_alert_history(humidity=request.args.get('Humidity'))
    if float(temperature[0]) > config.max_temperature:
        insert_to_alert_history(temperature=request.args.get('temperature'))

    return jsonify({"status": "OK"})



# @blueprints_v1.route('/set_stat_test', methods=['GET', 'POST'])
# def set_stat():
#     requests.post(url=API_ENDPOINT, data=data)

# endregion


# region get set screen
@blueprints_v1.route('/upload_file', methods=['GET', 'POST'])
def up_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            result = check_fatigue(file)
            print(result)
            save_data(result)
            resp = Response(json.dumps(result))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.mimetype = 'application/json'
            return resp
    return '''
                <!doctype html>
                <title>Upload new File</title>
                <h1>Upload new File</h1>
                <form action="" method=post enctype=multipart/form-data>
                  <p><input type=file name=file>
                     <input type=submit value=Upload>
                </form>
            '''


@blueprints_v1.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(config.UPLOAD_FOLDER,
                               filename)


@blueprints_v1.route('/get_current_signal')
def get_current_signal():
    res = get_last_signals()
    return jsonify(res)


@blueprints_v1.route('/get_all_signal')
def get_today_signal():
    res = get_all_signals()
    req = list()
    for i in res:
        print(i)
        req.append(i)
    req = json.dumps(req)
    resp = Response(req)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.mimetype='application/json'
    resp.content_encoding='UTF-8'
    return resp
    #return jsonify(res)

#
# @blueprints_v1.route('/get_all_signal')
# def get_today_signal():
#     res = get_all_signals()
#     return jsonify(res)




# region tech
@blueprints_v1.errorhandler(ValidationError)
def validation_json(error: ValidationError):
    return jsonify({'error': error.args[0]}), 400

#
# @blueprints_v1.errorhandler(Exception)
# def all_exception(error: Exception):
#     return jsonify({'error': error.args}), 520
# # endregion

# region messager


# region get set screen
dev_message = {
    'light': {'head': 'Темновато..', 'body': 'Работа за ПК в темноте портит вам зрение, включите свет', 'level': 'alert'},
    'micro': {'head': 'Шумно', 'body': 'Шум на вашем рабочем месте превышает допустимые нормы - бегите!', 'level': 'warning'},
    'sonar': {'head': 'Отодвиньтесь', 'body': 'Ваши глаза будут Вам благодарны, если вы отодвинетесь от экрана', 'level': 'alert'},
    'temperature': {'head': 'Очень влажно', 'body': 'Пора выключить увлажнитель воздуха!', 'level': 'warning'},
    'humidity': {'head': 'Очень жарко', 'body': 'Срочно нужно включить кондиционер или открыть окно', 'level': 'warning'},
    'fatigue': {'head': 'Вы устали!', 'body': 'Рекомендуется устроить небольшой перерыв', 'level': 'warning'}
}

# region get set screen
@blueprints_v1.route('/get_msg', methods=['GET'])
def get_msg():
    data = get_last_signals()
    print(data)
    req = list()
    for k, v in data.items():
        list_of_files = glob.glob(config.UPLOAD_FOLDER+'/*')
        img = max(list_of_files, key=os.path.getctime)
        img = img.split('/')[-1]
        req.append(
            {
                **dev_message[k],
                "img": img,
                **v
            }
        )
        insert_alert_to_database(dev_message[k]['head'], dev_message[k]['body'], img)
    req = json.dumps(req)
    resp = Response(req)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.mimetype='application/json'
    resp.content_encoding='UTF-8'
    return resp

    #return jsonify(req)
# endregion


