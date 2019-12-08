import os


class BaseConfig:
    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = ENV == "development"


class TestingConfig(BaseConfig):
    TESTING = True
