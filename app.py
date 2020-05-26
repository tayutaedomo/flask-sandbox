import os
from flask import Flask
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


if __name__ == '__main__':
    print('Config:', APP_SETTINGS)
    app.run()

