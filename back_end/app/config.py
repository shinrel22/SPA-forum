import os

# Instance folder path, makes it independent.
try:
    INSTANCE_FOLDER_PATH = os.path.join(os.getcwd(), 'tmp/instance')
    os.stat(INSTANCE_FOLDER_PATH)

except FileNotFoundError:
    os.makedirs(os.path.join(os.getcwd(), 'tmp/instance'))
    INSTANCE_FOLDER_PATH = os.path.join(os.getcwd(), 'tmp/instance')


class DefaultConfig(object):
    # Statement for enabling the development environment

    PROJECT = 'forums'

    # Get app root path, also can use flask.root_path.
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    ADMINS = ['trinm@vccloud.vn']

    # Upload file directory
    UPLOAD_DIR = os.path.abspath('app/static')

    DEBUG = True

    # Secret key for signing cookies
    SECRET_KEY = os.urandom(32)

    DB_URI = 'mysql+pymysql://root:813417@localhost:3306/forums'


class LocalConfig(DefaultConfig):
    URL_BASE = 'http://127.0.0.1:5000'
    FRONT_END_ROOT_URL = 'http://localhost:8080'


class DevConfig(DefaultConfig):
    URL_BASE = 'http://103.56.156.9:5000'
    FRONT_END_ROOT_URL = 'http://123.31.11.126:8080'


class StagingConfig(DefaultConfig):
    pass


class ProdConfig(DefaultConfig):
    pass


def get_config(chosenConfig=None):
    if not chosenConfig:
        chosenConfig = os.getenv('APPLICATION_MODE', 'LOCAL')

    SWITCH = {
        'LOCAL': LocalConfig,
        'DEV': DevConfig,
        'STAGING': StagingConfig,
        'PRODUCTION': ProdConfig,
    }
    return SWITCH[chosenConfig]
