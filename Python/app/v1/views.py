from marshmallow import ValidationError
from flask import Blueprint, request, jsonify, send_from_directory, Response

from app.libs.file_lib.upload_file import allowed_file, check_eyes
from app.libs.ml_lib.fatigue_checker import check_fatigue
from app.libs.sql_lib.insert_signal import insert_to_alert_history
from app.libs.sql_lib.get_signals import get_last_signals

import config as config

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
            upload = check_eyes(file)
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
    return jsonify(
        insert_to_alert_history(
            light=request.args.get('Light'),
            micro=request.args.get('microphoneValue'),
            sonar=request.args.get('Sonar'),
            humidity=request.args.get('Humidity'),
            temperature=request.args.get('temperature')
        )
    )

# @blueprints_v1.route('/set_stat_test', methods=['GET', 'POST'])
# def set_stat():
#     requests.post(url=API_ENDPOINT, data=data)
@blueprints_v1.route('/set_stat', methods=['GET', 'POST'])
def set_stat():
    if request.method == 'POST':
        return jsonify(insert_signal(request.json, request.date))
# endregion


# region get set screen
@blueprints_v1.route('/upload_file', methods=['GET', 'POST'])
def up_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            result = check_fatigue(file)
            upload = check_eyes(file, result)
            resp = Response(json.dumps(upload))
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
    return jsonify(get_last_signals())



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
@blueprints_v1.route('/get_msg', methods=['GET'])
def get_msg():
    img = '2019.09.28-20.30.07.jpeg'
    req = list()
    req.append({"head": "Вы устали!", "body": "Рекомендуется устроить небольшой перерыв", "img": img, "id": 3, "level": "danger"})
    req = json.dumps(req)
    resp = Response(req)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.mimetype='application/json'
    return resp
    #return jsonify(req)
# endregion
