from app import create_app
from config import Config, ConfigTesting

def test_app_created_for_tests():
    app = create_app(testing=True)
    assert app.config['SECRET_KEY'] == ConfigTesting.SECRET_KEY
    assert app.config['TESTING'] == ConfigTesting.TESTING
    assert app.config['SQLALCHEMY_DATABASE_URI'] == ConfigTesting.SQLALCHEMY_DATABASE_URI

def test_app_created():
    app = create_app()
    assert app.config['SECRET_KEY'] == Config.SECRET_KEY
    assert app.config['TESTING'] == Config.TESTING
    assert app.config['SQLALCHEMY_DATABASE_URI'] == Config.SQLALCHEMY_DATABASE_URI
    assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] == Config.SQLALCHEMY_TRACK_MODIFICATIONS
    assert app.config['PORT'] == Config.PORT
    assert app.config['SERVER'] == Config.SERVER