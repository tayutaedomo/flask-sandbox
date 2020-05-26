import os
import base64
from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
APP_SETTINGS = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(APP_SETTINGS)

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    u = os.getenv('BASICAUTH_USERNAME', 'sandbox')
    p = os.getenv('BASICAUTH_PASSWORD', 'flask')
    return username == u and password == p


@app.route('/')
@auth.login_required
def hello():
    return "Hello World!"


@app.route('/<name>')
@auth.login_required
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/form_file', methods=['GET'])
def form_file_get():
    local = {}

    return render_template('./form_file.html', local=local)


@app.route('/form_file', methods=['POST'])
def form_file_post():
    local = {}

    if request.files['image']:
        file = request.files['image']
        print(file)

        local['file'] = file
        local['file_body'] = request.files['image'].read()
        local['file_base64'] = str(base64.b64encode(local['file_body']), 'utf-8')
        print(local['file_base64'])

    return render_template('./form_file.html', local=local)


if __name__ == '__main__':
    print('Config:', APP_SETTINGS)
    app.run()

