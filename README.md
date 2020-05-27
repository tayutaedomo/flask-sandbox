# flask-sandbox
Try Flask

## Reference
- https://realpython.com/flask-by-example-part-1-project-setup/

## Setup
```
$ git clone git@github.com:tayutaedomo/flask-sandbox.git
$ cd flask-sandbox
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Local Server
```
$ cd flask-sandbox
$ python app.py
$ open "http://127.0.0.1:5000/"
```
Basic Auth: sandbox / flask

## Config ENV
You should set the appropriate ENV.
```
$ export APP_SETTINGS="config.DevelopmentConfig"
# or
$ export APP_SETTINGS=config.StagingConfig
# or
$ export APP_SETTINGS=config.ProductionConfig
```

