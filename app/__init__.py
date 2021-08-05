from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(TESTING=False,
                            DEBUG=True,
                            SECRET_KEY='secret_key',
                            SERVER='0.0.0.0')
    return app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)