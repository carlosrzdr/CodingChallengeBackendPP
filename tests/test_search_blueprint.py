from app.actions.plate_actions import row2dict
from app import create_app
from app.models import Plate

def test_search_plate_get_request_success(session):
    app = create_app(testing=True)

    with app.test_client() as test_client:
        expected_plate = Plate('M-PP123')
        search_plate_number = 'MM-PP123'
        session.add(expected_plate)
        session.commit()
        response = test_client.get("/search-plate?key={}&levenshtein=1".format(search_plate_number))
        assert eval(response.data) == [row2dict(expected_plate)]

def test_search_plate_get_request_success_empty(session):
    app = create_app(testing=True)
    with app.test_client() as test_client:
        expected_plate = Plate('M-PP123')
        search_plate_number = 'MM-PP1234'
        session.add(expected_plate)
        session.commit()
        response = test_client.get("/search-plate?key={}&levenshtein=1".format(search_plate_number))
        assert eval(response.data) == []

def test_search_plate_get_request_malformed_request():
    app = create_app(testing=True)

    with app.test_client() as test_client:
        response = test_client.get("/search-plate?key=&levenshtein=")
        assert response.status_code == 400

def test_search_plate_get_request_malformed_plate():
    app = create_app(testing=True)

    with app.test_client() as test_client:
        response = test_client.get("/search-plate?key=ABC123&levenshtein=1")
        assert response.status_code == 422