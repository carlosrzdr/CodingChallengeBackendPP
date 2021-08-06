from app.plate import plateIsValid

def test_plate_validation_correct():
    plate_number = 'M-PP123'
    assert plateIsValid(plate_number) != None

def test_plate_validation_error():
    plate_number = 'M-PP0123'
    assert plateIsValid(plate_number) == None