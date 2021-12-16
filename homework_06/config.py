import os

SQLALCHEMY_DATABASE_URI=os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://app:password@localhost:5432/calendar",
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False


class DevelopmentConfig(Config):
    Debug = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
