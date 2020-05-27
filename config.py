#import os
#basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ENV = 'production'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024    # 5MB


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    ENV = 'staging'
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True

