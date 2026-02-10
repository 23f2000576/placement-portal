import os

class Config:
    SECRET_KEY = "secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///../instance/placement.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis (for caching & celery)
    REDIS_URL = "redis://localhost:6379/0"
