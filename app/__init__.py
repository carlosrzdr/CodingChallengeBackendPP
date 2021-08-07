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
        from app import plate, search_plate # Import views here to avoid circular importing
        db.create_all()
        app.register_blueprint(plate.bp)
        app.register_blueprint(search_plate.bp)

        return app
