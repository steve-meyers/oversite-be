import json
from app import app
import vcr

test_browser = app.test_client()

def test_it_returns_users():
    global test_browser
    response = test_browser.get('/users')
    assert response.status_code == 200
    assert type(json.loads(response.data)) is list

def test_it_returns_members_by_state():
    global test_browser
    state = 'co'
    with vcr.use_cassette('fixtures/vcr_cassettes/members_by_state.yaml'):
      response = test_browser.get(f'/members_by_state/{state}')

    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert type(response_data) is dict

    assert type(response_data['results'][0]['senate']) is list
    assert response_data['results'][0]['senate'][0]['id'] == 'G000562'
    assert response_data['results'][0]['senate'][0]['first_name'] == 'Cory'
    assert response_data['results'][0]['senate'][0]['last_name'] == 'Gardner'
    assert response_data['results'][0]['senate'][0]['image'] == 'https://theunitedstates.io/images/congress/original/G000562.jpg'
    assert response_data['results'][0]['senate'][0]['party'] == 'Republican'
    assert response_data['results'][0]['senate'][0]['role'] == 'Senator, 2nd Class'

    assert type(response_data['results'][1]['house']) is list
    assert response_data['results'][1]['house'][0]['id'] == 'D000197'
    assert response_data['results'][1]['house'][0]['first_name'] == 'Diana'
    assert response_data['results'][1]['house'][0]['last_name'] == 'DeGette'
    assert response_data['results'][1]['house'][0]['image'] == 'https://theunitedstates.io/images/congress/original/D000197.jpg'
    assert response_data['results'][1]['house'][0]['party'] == 'Democrat'
    assert response_data['results'][1]['house'][0]['role'] == 'Representative'

def test_it_returns_users_members():
    global test_browser
    user_id = 1
    with vcr.use_cassette('fixtures/vcr_cassettes/users_reps.yaml'):
      response = test_browser.get(f'/users_reps/{user_id}')

    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert type(response_data) is dict
    assert type(response_data['results'][0]['senate']) is list
    assert response_data['results'][0]['senate'][0]['image'] == 'https://theunitedstates.io/images/congress/original/G000562.jpg'
    assert response_data['results'][0]['senate'][0]['id'] == 'G000562'
    assert response_data['results'][0]['senate'][0]['first_name'] == 'Cory'
    assert response_data['results'][0]['senate'][0]['last_name'] == 'Gardner'

    assert response_data['results'][0]['senate'][0]['party'] == 'Republican'
    assert response_data['results'][0]['senate'][0]['role'] == 'Senator, 2nd Class'

    assert type(response_data['results'][1]['house']) is list
    assert response_data['results'][1]['house'][0]['id'] == 'P000593'
    assert response_data['results'][1]['house'][0]['first_name'] == 'Ed'
    assert response_data['results'][1]['house'][0]['last_name'] == 'Perlmutter'
    assert response_data['results'][1]['house'][0]['image'] == 'https://theunitedstates.io/images/congress/original/P000593.jpg'
    assert response_data['results'][1]['house'][0]['party'] == 'Democrat'
    assert response_data['results'][1]['house'][0]['role'] == 'Representative'

def test_it_returns_member_details():
    global test_browser
    member_id = 'G000562'

    with vcr.use_cassette('fixtures/vcr_cassettes/member_details.yaml'):
      response = test_browser.get(f'/member/{member_id}')
      response_data = json.loads(response.data)

    assert response.status_code == 200
    assert type(response_data) is dict
    assert 'results' in response_data
    assert response_data.get('results')[0]['id'] == 'G000562'
    assert response_data.get('results')[0]['first_name'] == 'Cory'
    assert response_data.get('results')[0]['last_name'] == 'Gardner'
    assert response_data.get('results')[0]['role'] == 'Senator, 2nd Class'
    assert response_data.get('results')[0]['phone'] == '202-224-5941'
    assert response_data.get('results')[0]['address'] == '354 Russell Senate Office Building'
    assert response_data.get('results')[0]['twitter_url'] == 'https://twitter.com/SenCoryGardner'
    assert response_data.get('results')[0]['twitter_handle'] == 'SenCoryGardner'
    assert response_data.get('results')[0]['youtube'] == None
    assert response_data.get('results')[0]['facebook'] == 'https://www.facebook.com/SenCoryGardner'
    assert response_data.get('results')[0]['party'] == 'Republican'
    assert response_data.get('results')[0]['chamber'] == 'Senate'
    assert response_data.get('results')[0]['state'] == 'CO'
    assert response_data.get('results')[0]['district'] == None
    assert response_data.get('results')[0]['website'] == 'https://www.gardner.senate.gov'
    assert response_data.get('results')[0]['contact_form_url'] == 'https://www.gardner.senate.gov/contact-cory/email-cory'

def test_it_sends_tweet_to_microservice():
    global test_browser
    handle = 'smj289'
    message = 'This is the last test tweet we need to send'

    with vcr.use_cassette('fixtures/vcr_cassettes/tweet.yaml'):
      response = test_browser.get(f'/tweet?handle={handle}&message={message}')
      response_data = json.loads(response.data)

    assert 'Message sent' == response_data.get('message')
