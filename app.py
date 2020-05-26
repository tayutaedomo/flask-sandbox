import os
from flask import Flask

app = Flask(__name__)
APP_SETTINGS = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(APP_SETTINGS)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    print('Config:', APP_SETTINGS)
    app.run()

