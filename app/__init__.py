from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(testing=False):
    app = Flask(__name__, instance_relative_config=True)
    if testing:
        app.config.from_object('config.Config')
    else:
        app.config.from_object('config.ConfigTesting')

    db.init_app(app)

    with app.app_context():
        db.create_all()
        return app
