import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()
API_URL = 'https://www.wikidata.org/w/api.php'


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/get-entity/{search_str}')
def get_entity(search_str: str):
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

    return results[0]


@app.get('/get-claims/{search_str}')
def get_claims(search_str: str):
    """Return the claims of the search string from the MediaWiki API."""
    entity = get_entity(search_str)['id']
    response = requests.get(API_URL, params={'action': 'wbgetclaims',
                                             'entity': entity,
                                             'format': 'json'})
    # TODO: Write tests
    # TODO: Include test for no results
    results = response.json()['claims']
    if not results:
        raise HTTPException(status_code=404, detail='No results found')

    return results
