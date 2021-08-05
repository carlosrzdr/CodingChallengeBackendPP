from app import database
import datetime

class Plate(database.Model):
    
    id = database.Column(database.Integer, primary_key=True)
    plate = database.Column(database.String(10), nullable=False)
    timestamp = database.Column(database.DateTime, default=datetime.datetime.now())

    def __init__(self, plate):
        self.plate = plate

def create_plate(plate_number):

    plate = Plate(plate_number)
    database.session.add(plate)
    database.session.commit()

    return plate


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    database.create_all()
    print("Done!")