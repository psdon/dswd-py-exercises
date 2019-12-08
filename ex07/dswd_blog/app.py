from flask import Flask
from . import auth, public, config
import logging, sys


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevConfig)

    app.register_blueprint(auth.views.bp)
    app.register_blueprint(public.views.bp)
    return app


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
