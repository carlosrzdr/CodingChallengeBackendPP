from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.views import view

db = SQLAlchemy()

def create_app(testing=False):
    app = Flask(__name__, instance_relative_config=True)
    if testing:
        app.config.from_object('config.ConfigTesting')
    else:
        app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()
        app.register_blueprint(view)
        return app
