from app.plate import plate_is_valid, search_plate_levenshtein, row2dict, get_plates
from app.models import Plate

def test_plate_validation_correct():
    plate_number = 'M-PP123'
    assert plate_is_valid(plate_number) != None

def test_plate_validation_error():
    no_number_plate_number = 'M-PP'
    start_zero_plate_number = 'M-PP0123'
    too_many_numbers_plate_number = 'M-PP12345'
    before_hyphen_letters_plate_number = 'MMMM-PP123'
    after_hyphen_letters_plate_number = 'MMMM-PP123'

    assert plate_is_valid(no_number_plate_number) == None
    assert plate_is_valid(start_zero_plate_number) == None
    assert plate_is_valid(too_many_numbers_plate_number) == None
    assert plate_is_valid(before_hyphen_letters_plate_number) == None
    assert plate_is_valid(after_hyphen_letters_plate_number) == None

def test_search_plate_levenshtein_found(session):
    expected_plate = Plate('M-PP123')
    session.add(expected_plate)
    session.commit()
    searched_plate_levenshtein_1 = 'MM-PP123'
    searched_plate_levenshtein_2 = 'Q-PP1234'

    assert search_plate_levenshtein(searched_plate_levenshtein_1, 1) == [{'id':str(expected_plate.id), 'plate': str(expected_plate.plate), 'timestamp': str(expected_plate.timestamp)}]
    assert search_plate_levenshtein(searched_plate_levenshtein_2, 2) == [{'id':str(expected_plate.id), 'plate': str(expected_plate.plate), 'timestamp': str(expected_plate.timestamp)}]

def test_search_plate_levenshtein_not_found(session):
    expected_plate = Plate('M-PP123')
    session.add(expected_plate)
    session.commit()
    searched_plate_levenshtein = 'MMM-PP123'

    assert search_plate_levenshtein(searched_plate_levenshtein, 1) == []

def test_get_plates(session):
    expected_plate = Plate('M-PP123')
    session.add(expected_plate)
    session.commit()

    assert get_plates() == [{'id':str(expected_plate.id), 'plate': str(expected_plate.plate), 'timestamp': str(expected_plate.timestamp)}]

def test_get_plates_empty(session):
    assert get_plates() == []

def test_row2dict():
    expected_plate = Plate('M-PP123')
    assert row2dict(expected_plate) == {'id':str(expected_plate.id), 'plate': str(expected_plate.plate), 'timestamp': str(expected_plate.timestamp)}