from typing import Optional
import requests


API_URL = 'https://www.wikidata.org/w/api.php'


def get_entity(search_str: str) -> dict[str, list]:
    """Return the top result of the search string from the MediaWiki API."""
    response = requests.get(API_URL, params={'action'  : 'wbsearchentities',
                                             'search'  : search_str,
                                             'language': 'en',
                                             'format'  : 'json'})
    # TODO: Write tests
    # TODO: Include test for no results
    results = response.json()['search']

    return results[0]


def get_claims(search_str: str, prop: Optional[str] = '') -> dict[str, list]:
    """Return the claims of the search string from the MediaWiki API."""
    entity = get_entity(search_str)['id']
    params = {'action': 'wbgetclaims',
            'entity': entity,
            'format': 'json'}

    if prop:
        params['property'] = prop

    response = requests.get(API_URL, params=params)
    # TODO: Write tests
    # TODO: Include test for no results
    results = response.json()['claims']

    return results


def get_ids(items: list[str]) -> list[str]:
    """Return list of IDs of the top result for each given string."""
    return [get_entity(item)['id'] for item in items]


def get_labels(items: list[str]) -> list[str]:
    """Return list of labels for each corresponding ID given."""
    response = requests.get(API_URL, params={'action': 'wbgetentities',
                                             'ids'   : '|'.join(items),
                                             'props' : 'labels',
                                             'format': 'json'})
    return [e['labels']['en']['value']
            for e in response.json()['entities'].values()]
