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
from services.propublica import PropublicaService
from classes.member_index import MemberIndex
from classes.member_show import MemberShow

@app.route("/")
def hello():
    return "Welcome to the OverSite API"


@app.route("/add_new_user", methods = ['POST'])
def add_user():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    street_address = request.args.get('street_address')
    state = request.args.get('state')
    zip = request.args.get('zip')
    district = request.args.get('district')

    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            street_address=street_address,
            state=state,
            zip=zip,
            district=district
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
    senate_results = PropublicaService.senators_by_state(state_)
    house_results = PropublicaService.reps_by_state(state_)

    senator_objects = map(lambda result: MemberIndex(result), senate_results)

    rep_objects = map(lambda result: MemberIndex(result), house_results)

    senators = list(senator_objects)
    reps = list(rep_objects)

    try:
        return jsonify({"results":
        [{"senate": list(map(lambda member: member.serialize(), senators))},
        {"house": list(map(lambda member: member.serialize(), reps))}]
        })

    except Exception as e:
        return(str(e))

@app.route("/users_reps/<user_id_>")
def get_users_reps(user_id_):
    user = User.query.filter_by(id=user_id_).first()

    senate_results = PropublicaService.senators_by_state(user.state)
    house_results = PropublicaService.reps_by_district(user.state, user.district)

    senator_objects = map(lambda result: MemberIndex(result), senate_results)

    rep_objects = map(lambda result: MemberIndex(result), house_results)

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
    result = PropublicaService.member_details(id_)
    member = MemberShow(result)

    try:
        return jsonify({'results': [member.serialize()]})
    except Exception as e:
        return(str(e))

@app.route("/tweet")
def get_message_sent_to_twitter():
    handle = request.args.get('handle', None)
    message = request.args.get('message', None)
    URL = f'https://gentle-falls-99830.herokuapp.com/send-tweet?message={message}&handle={handle}'
    response = requests.get(URL).json()
    try:
        return response
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()
