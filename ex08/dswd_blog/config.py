import os


class BaseConfig:
    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = ENV == "development"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
