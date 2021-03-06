from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

class Config:
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER = os.getenv('SERVER')
    PORT = os.getenv('PORT')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///plates.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

class ConfigTesting(Config):
    TESTING = True
    SECRET_KEY = os.getenv('TEST_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'