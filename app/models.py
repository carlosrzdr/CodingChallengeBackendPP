from app import db
import datetime

class Plate(db.Model):

    __tablename__ = 'plates'
    
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    plate = db.Column(
        db.String(10), 
        nullable=False
    )
    timestamp = db.Column(
        db.DateTime,
        nullable=False
    )

    def __init__(self, plate_number):
        self.plate = plate_number
        self.timestamp = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()