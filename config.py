import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key-for-garden-app')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:ashes12@localhost/garden_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
