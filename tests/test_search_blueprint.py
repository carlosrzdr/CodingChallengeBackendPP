from app.actions.plate_actions import row2dict
from app.models import Plate

def test_search_plate_get_request_success(session, app):
    with app.test_client() as test_client:
        expected_plate = Plate('M-PP123')
        search_key = 'MMPP123'
        session.add(expected_plate)
        session.commit()
        response = test_client.get("/search-plate?key={}&levenshtein=1".format(search_key))
        assert eval(response.data) == [row2dict(expected_plate)]

def test_search_plate_get_request_success_empty(session, app):
    with app.test_client() as test_client:
        expected_plate = Plate('M-PP123')
        search_key = 'MMPP1234'
        session.add(expected_plate)
        session.commit()
        response = test_client.get("/search-plate?key={}&levenshtein=1".format(search_key))
        assert eval(response.data) == []

def test_search_plate_get_request_malformed_request(app):
    with app.test_client() as test_client:
        all_fields_empty_response = test_client.get("/search-plate?key=&levenshtein=")
        key_field_empty_response = test_client.get("/search-plate?key=&levenshtein=")
        levenshtein_field_empty_response = test_client.get("/search-plate?key=&levenshtein=")
        assert all_fields_empty_response.status_code == 400
        assert key_field_empty_response.status_code == 400
        assert levenshtein_field_empty_response.status_code == 400

def test_search_page_found(app):
    with app.test_client() as test_client:
        response = test_client.get('/search')
        assert response.status_code == 200