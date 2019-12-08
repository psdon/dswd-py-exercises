from flask import Flask
from . import auth, public, config


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config.from_object(config.TestingConfig)

    app.register_blueprint(auth.views.bp)
    app.register_blueprint(public.views.bp)
    return app
