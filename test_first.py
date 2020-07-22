import pytest
import requests
import json
from app import app

test_browser = app.test_client()

url = 'http://127.0.0.1:5000'

def test_index_page():
    global test_browser
    response = test_browser.get('/')

    assert response.status_code == 200

def test_it_returns_users():
    global test_browser
    response = test_browser.get('/users')
    assert response.status_code == 200
    assert type(json.loads(response.data)) is list
