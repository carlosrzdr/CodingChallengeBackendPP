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
        default=datetime.datetime.now()
    )

    def __init__(self, plate):
        self.plate = plate

    def save(plate_number):

        plate = Plate(plate_number)
        db.session.add(plate)
        db.session.commit()

        return plate