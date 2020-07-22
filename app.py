import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import code

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User
from classes import MemberIndex

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
    headers = {'X-API-Key': 'JBIDWEsRXZPkQJPUHkaH5t26psMcJxS2x8kOPh0A'}
    URL = f'https://api.propublica.org/congress/v1/members/senate/{state_}/current.json'
    response = requests.get(URL, headers = headers).json()
    results = response['results']
    
    # members = results.map do |result|
    #   MemberIndex(first_name = result['first_name'],
    #               last_name =result['last_name'],
    #               role = result['role'],
    #               party = result['party'])
    # end
    
    
    objects = map(lambda result: MemberIndex(first_name = result['first_name'],
                                   party = result['party'],
                                   role = result['role'],
                                   last_name =result['last_name']),
                                   results)
    list_of_members = list(objects)
    code.interact(local=dict(globals(), **locals()))
    
    try:
        return jsonify(test[0])


        # return jsonify(first_name=member.first_name,
        #                last_name=member.last_name,
        #                role=member.role,
        #                party=member.party)
    except Exception as e:
	    return(str(e))


if __name__ == '__main__':
    app.run()
