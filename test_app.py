import json
from app import app
import random

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
    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert type(response_data) is dict
    
    assert type(response_data['results'][0]['senate']) is list
    assert 'id' in response_data['results'][0]['senate'][0]
    assert 'first_name' in response_data['results'][0]['senate'][0]
    assert 'last_name' in response_data['results'][0]['senate'][0]
    assert 'party' in response_data['results'][0]['senate'][0]
    assert 'role' in response_data['results'][0]['senate'][0]
    
    assert type(response_data['results'][1]['house']) is list
    assert 'id' in response_data['results'][1]['house'][0]
    assert 'first_name' in response_data['results'][1]['house'][0]
    assert 'last_name' in response_data['results'][1]['house'][0]
    assert 'party' in response_data['results'][1]['house'][0]
    assert 'role' in response_data['results'][1]['house'][0]

def test_it_returns_member_details():
    global test_browser
    member_id = 'G000562'
    response = test_browser.get(f'/member/{member_id}')
    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert type(response_data) is dict
    assert 'results' in response_data
    assert 'id' in response_data.get('results')[0]
    assert 'first_name' in response_data.get('results')[0]
    assert 'last_name' in response_data.get('results')[0]
    assert 'role' in response_data.get('results')[0]
    assert 'phone' in response_data.get('results')[0]
    assert 'address' in response_data.get('results')[0]
    assert 'twitter_url' in response_data.get('results')[0]
    assert 'twitter_handle' in response_data.get('results')[0]
    assert 'youtube' in response_data.get('results')[0]
    assert 'facebook' in response_data.get('results')[0]
    assert 'party' in response_data.get('results')[0]
    assert 'chamber' in response_data.get('results')[0]
    assert 'state' in response_data.get('results')[0]
    assert 'district' in response_data.get('results')[0]
    assert 'website' in response_data.get('results')[0]
    assert 'contact_form_url' in response_data.get('results')[0]

    def test_it_sends_tweet_to_microservice():
        f = ['cool', 'great', 'awesome', 'chill', 'dude', 'yes', 'yazy']
        for i in range(99999):
            rand_num = random.choice(i, end=', ')
        rand = random.choice(f)
        global test_browser
        handle = 'smj289'
        message = f'hello {rand} steven{rand_num}'
        response = test_browser.get(f'/tweet?{handle}&{message}')
        response_data = json.loads(response.data)

        assert 'message sent' == response_data
