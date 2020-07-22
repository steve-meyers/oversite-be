import json
from app import app

test_browser = app.test_client()

def test_index_page():
    global test_browser
    response = test_browser.get('/')
    assert response.status_code == 200

def test_it_returns_users():
    global test_browser
    response = test_browser.get('/users')
    assert response.status_code == 200
    assert type(json.loads(response.data)) is list

def test_it_returns_members_by_state():
    global test_browser
    state = 'co'
    response = test_browser.get(f'/members_by_state/{state}')
    assert response.status_code == 200
    assert type(json.loads(response.data)) is dict
