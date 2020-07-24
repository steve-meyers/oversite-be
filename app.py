import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests
import json
import code
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User
from classes import MemberIndex, MemberShow

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/add_new_user", methods = ['POST'])
def add_user():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    street_address = request.args.get('street_address')
    state = request.args.get('state')
    zip = request.args.get('zip')
    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            street_address=street_address,
            state=state,
            zip=zip
        )
        db.session.add(user)
        db.session.commit()
        return "User added. user id={}".format(user.id)
    except Exception as e:
	    return(str(e))


@app.route("/users")
def get_all():
    try:
        users = User.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
	    return(str(e))


@app.route("/user/<id_>")
def get_by_id(id_):
    try:
        user = User.query.filter_by(id=id_).first()
        return jsonify(user.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/members_by_state/<state_>")
def get_members_by_state(state_):
    headers = {'X-API-Key': os.getenv('PROP_API')}
    URL_SENATE = f'https://api.propublica.org/congress/v1/members/senate/{state_}/current.json'
    URL_HOUSE = f'https://api.propublica.org/congress/v1/members/house/{state_}/current.json'
    senate_response = requests.get(URL_SENATE, headers = headers).json()
    house_response = requests.get(URL_HOUSE, headers = headers).json()
    senate_results = senate_response['results']
    house_results = house_response['results']

    senator_objects = map(lambda result: MemberIndex(id = result['id'],
                                                     first_name = result['first_name'],
                                                     party = result['party'],
                                                     role = result['role'],
                                                     last_name =result['last_name']),
                                                     senate_results)

    rep_objects = map(lambda result: MemberIndex(id = result['id'],
                                                 first_name = result['first_name'],
                                                 party = result['party'],
                                                 role = result['role'],
                                                 last_name =result['last_name']),
                                                 house_results)
                          
    senators = list(senator_objects)
    reps = list(rep_objects)

    try:
        return jsonify({"results": 
        [{"senate": list(map(lambda member: member.serialize(), senators))}, 
        {"house": list(map(lambda member: member.serialize(), reps))}]
        })

    except Exception as e:
	    return(str(e))

@app.route("/member/<id_>")
def get_member_details(id_):
    headers = {'X-API-Key': os.getenv('PROP_API')}
    URL = f'https://api.propublica.org/congress/v1/members/{id_}.json'
    response = requests.get(URL, headers = headers).json()
    result = response['results'][0]
    
    district = None
    if result['roles'][0]['chamber'] == 'House':
      district = result['roles'][0]['district']
    
    member = MemberShow(id = result['id'],
               first_name = result['first_name'],
               last_name = result['last_name'],
               role = result['roles'][0]['title'],
               phone = result['roles'][0]['phone'],
               address = result['roles'][0]['office'],
               twitter = result['twitter_account'],
               youtube = result['youtube_account'],
               facebook = result['facebook_account'],
               party = result['roles'][0]['party'],
               chamber = result['roles'][0]['chamber'],
               state = result['roles'][0]['state'],
               district = district,
               website = result['url'],
               contact_form_url = result['roles'][0]['contact_form'])
    try:
        return jsonify({'results': [member.serialize()]})
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()
