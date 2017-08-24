from flask import Flask
from .api import endpoints
from .config import DefaultConfig, INSTANCE_FOLDER_PATH
from .extensions import db, api

__all__ = ['create_app']

DEFAULT_BLUEPRINTS = [
    endpoints
]


def create_app(config=None, app_name=None, blueprints=None):
    """Create app dua vao config, app_name va blueprints
    """

    if not config:
        config = DefaultConfig

    if not app_name:
        app_name = config.PROJECT

    if not blueprints:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name,
                instance_path=INSTANCE_FOLDER_PATH,
                instance_relative_config=True)

    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app, config)
    configure_logging(app)
    configure_error_handlers(app)
    return app


def configure_app(app, config):
    if not config:
        app.config.from_object(DefaultConfig)
        return

    app.config.from_object(config)


def configure_extensions(app, config):
    if not config:
        config = DefaultConfig

    # flask_restful
    api.init_app(app)

    # database
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_logging(app):
    # app.logger.addHandler(file_handler)
    # app.logger.debug()
    pass


def configure_hook(app):
    """configure_hook regist hook in app like before_request, after_request

        :param app:
    """
    @app.before_request
    def before_request():
        """ This function runs when app receives a request before endpoint. """
        return


def configure_error_handlers(app):
    @app.errorhandler(500)
    def server_error_page(error):
        return "ERROR PAGE!"
