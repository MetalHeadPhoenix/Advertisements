import os 
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__name__))
    #Swagger Configs
    API_TITLE = os.getenv('API_TITLE')
    API_VERSION = os.getenv('API_VERSION')
    OPENAPI_VERSION = os.getenv('OPENAPI_VERSION')
    OPENAPI_URL_PREFIX = os.getenv('OPENAPI_URL_PREFIX')
    OPENAPI_SWAGGER_UI_PATH = os.getenv('OPENAPI_SWAGGER_UI_PATH')
    OPENAPI_SWAGGER_UI_URL = os.getenv('OPENAPI_SWAGGER_UI_URL')
    OPENAPI_REDOC_PATH = os.getenv('OPENAPI_REDOC_PATH')
    OPENAPI_REDOC_UI_URL = os.getenv('OPENAPI_REDOC_UI_URL')
    #Flask Babel Configs
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(BASE_DIR, 'translations')
    #Swagger Authentication (JWT Configs)
    API_SPEC_OPTIONS = {
        'security':[{"bearerAuth": []}],
        'components':{
            "securitySchemes":
                {
                    "bearerAuth": {
                        "type":"http",
                        "scheme": "bearer",
                        "bearerFormat": "JWT"
                    }
                }
        }
    }

class Config(BaseConfig):
    CSRF = os.getenv('CSRF')
    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')

class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCTION_SQLALCHEMY_DATABASE_URI')
    
class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_SQLALCHEMY_DATABASE_URI')

class Test(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'tests','test.db')
    