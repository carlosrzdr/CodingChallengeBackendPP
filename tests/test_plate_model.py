from app.models import Plate

def test_plate_entry_created(session):
    plate = Plate(plate='a-plate')

    session.add(plate)
    session.commit()

    assert plate.id > 0

def test_plate_found(session):
    plate = Plate(plate='a-plate')

    session.add(plate)
    session.commit()

    found_plate = Plate.query.filter_by(plate=plate.plate).first()

    assert found_plate == plate