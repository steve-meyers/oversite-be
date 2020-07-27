import os
import requests
import json
import code
import dotenv

dotenv.load_dotenv()

class PropublicaService:

    def conn():
        headers = {'X-API-Key': os.getenv('PROP_API')}

    def member_details(id_):
        headers = {'X-API-Key': os.getenv('PROP_API')}
        URL = f'https://api.propublica.org/congress/v1/members/{id_}.json'
        return (requests.get(URL, headers=headers).json())['results'][0]

    def senators_by_state(state_):
        headers = {'X-API-Key': os.getenv('PROP_API')}
        URL = f'https://api.propublica.org/congress/v1/members/senate/{state_}/current.json'
        return (requests.get(URL, headers=headers).json())['results']

    def reps_by_state(state_):
        headers = {'X-API-Key': os.getenv('PROP_API')}
        URL = f'https://api.propublica.org/congress/v1/members/house/{state_}/current.json'
        return (requests.get(URL, headers=headers).json())['results']

    def reps_by_district(state_, district_):
        headers = {'X-API-Key': os.getenv('PROP_API')}
        URL = f'https://api.propublica.org/congress/v1/members/house/{state_}/{district_}/current.json'
        return (requests.get(URL, headers=headers).json())['results']

