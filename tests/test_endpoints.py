import pytest
import requests
    import code

url = 'http://127.0.0.1:5000'  # The root url of the flask app


def test_index_page():
    r = requests.get(url+'/users')  # Assumses that it has a path of "/"
   code.interact(local=locals())
    # assert r.status_code == 200  # Assumes that it will return a 200 response
