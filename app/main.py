"""
Simple fastAPI for testing mock requests
"""

import fastapi
from app import retrieve


app = fastapi.FastAPI()


@app.get('/')
def root_entry():
    """root entry route"""
    return "hello world"

@app.get('/taf/{icao}')
def taf_bounce(icao):
    """ test user input"""
    return {"msg":icao}

@app.get('/test')
def test_retrieve():
    """blend class to route"""
    test = retrieve.Retrieve()
    data = test.get_data()
    return data
