from app.actions.plate_actions import row2dict
from app.models import Plate

def test_plate_get_request(session, app):
    with app.test_client() as test_client:
        expected_plate = Plate('M-PP123')
        session.add(expected_plate)
        session.commit()
        response = test_client.get('/plate')
        assert eval(response.data) == [row2dict(expected_plate)]

def test_plate_get_request_empty(app, session):
    with app.test_client() as test_client:
        response = test_client.get('/plate')
        assert eval(response.data) == []

def test_plate_post_request_success(session, app):
    with app.test_client() as test_client:
        expected_plate = Plate('M-PP123')
        session.add(expected_plate)
        session.commit()
        response = test_client.post('/plate', data = {'plate': 'M-PP123'})
        assert response.status_code == 200
    
def test_plate_post_request_not_valid_plate(app):
    with app.test_client() as test_client:
        response = test_client.post('/plate', data = {'plate': 'M-PPP123'})
        assert response.status_code == 422 

def test_plate_post_request_malformed_json(app):
    with app.test_client() as test_client:
        response = test_client.post('/plate', data = {})
        assert response.status_code == 400

def test_plates_page_found(app):
    with app.test_client() as test_client:
        response = test_client.get('/plates')
        assert response.status_code == 200
