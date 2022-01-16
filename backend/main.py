import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()
API_URL = 'https://www.wikidata.org/w/api.php'


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/{search_str}')
def get_node(search_str: str):
    """Return the top result of the search string from the MediaWiki API."""
    response = requests.get(API_URL, params={'action': 'wbsearchentities',
                                             'search': search_str,
                                             'language': 'en',
                                             'format': 'json'})
    # TODO: Write tests
    # TODO: Include test for no results
    results = response.json()['search']
    if not results:
        raise HTTPException(status_code=404, detail='No results found')

    return response.json()['search'][0]
