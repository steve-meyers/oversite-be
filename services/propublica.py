import os
import requests
import json
import dotenv

dotenv.load_dotenv()

class PropublicaService:
    @staticmethod
    def member_details(id_):
        endpoint = f'{id_}.json'
        url = PropublicaService.__base_url() + endpoint
        headers = PropublicaService.__headers()
        return (requests.get(url, headers = headers).json())['results'][0]

    @staticmethod
    def senators_by_state(state_):
        endpoint = f'senate/{state_}/current.json'
        url = PropublicaService.__base_url() + endpoint
        headers = PropublicaService.__headers()
        return (requests.get(url, headers = headers).json())['results']

    @staticmethod
    def reps_by_state(state_):
        endpoint = f'house/{state_}/current.json'
        url = PropublicaService.__base_url() + endpoint
        headers = PropublicaService.__headers()
        return (requests.get(url, headers = headers).json())['results']

    @staticmethod
    def reps_by_district(state_, district_):
        endpoint = f'house/{state_}/{district_}/current.json'
        url = PropublicaService.__base_url() + endpoint
        headers = PropublicaService.__headers()
        return (requests.get(url, headers = headers).json())['results']

    @staticmethod
    def __headers():
        return {'X-API-Key': os.getenv('PROP_API')}

    @staticmethod
    def __base_url():
        return 'https://api.propublica.org/congress/v1/members/'
