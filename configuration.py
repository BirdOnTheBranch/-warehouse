class BaseConfig(object):
    'Base configuration'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
class ProductionConfig(BaseConfig):
    'Producction configuration'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Develop configuration'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'