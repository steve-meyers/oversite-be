import pytest
import requests

url = 'http://127.0.0.1:5000'

def test_index_page():
    r = requests.get(url+'/')
    assert r.status_code == 200

def test_it_returns_users():
    r = requests.get(url+'/users')
    assert r.status_code == 200