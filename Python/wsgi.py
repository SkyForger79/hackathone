from flask_runner import get_app
import config

app = get_app()

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
    #app.run(debug=True, host='localhost', port=9999)
    #app.run(debug=True, host='10.70.13.34', port=9999)
    app.run(debug=True, host='192.168.0.103', port=9999)
