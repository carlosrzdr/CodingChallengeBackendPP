from app.models import Plate

def test_plate_entry_created(session):
    plate = Plate(plate_number='plate-created')

    session.add(plate)
    session.commit()

    assert plate.id > 0

def test_plate_found(session):
    expected_plate = Plate(plate_number='plate-found')

    session.add(expected_plate)
    session.commit()

    found_plate = Plate.query.filter_by(plate=expected_plate.plate).first()

    assert found_plate == expected_plate