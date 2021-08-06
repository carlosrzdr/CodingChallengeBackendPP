from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(testing=None):
    app = Flask(__name__)
    if testing:
        app.config.from_object('config.Config')
    else:
        app.config.from_object('config.ConfigTesting')

    db.init_app(app)

    with app.app_context():
        from app.views import view # Import views here to avoid circular importing
        db.create_all()
        app.register_blueprint(view)

        return app
