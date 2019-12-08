from flask import Flask
from . import auth, public


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth.views.bp)
    app.register_blueprint(public.views.bp)
    return app
