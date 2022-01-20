import requests
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse


API_URL = 'https://www.wikidata.org/w/api.php'
router = APIRouter()


@router.get('/')
def read_root():
    return {'Hello': 'World'}


@router.get('/get-entity/{search_str}')
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


@router.get('/get-claims/{search_str}')
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


@router.get('/get-page/{search_str}')
def get_page(search_str: str):
    """Return the claims of the search string from the MediaWiki API."""
    # TODO: Write tests
    # TODO: Include test for no results
    return RedirectResponse(get_entity(search_str)['url'])
