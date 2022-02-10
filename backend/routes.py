from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse
import finder
import utils


router = APIRouter()


@router.get('/')
def read_root():
    return {'Hello': 'World'}


@router.get('/get-entity/{search_str}')
def get_entity(search_str: str):
    results = utils.get_entity(search_str)
    if not results:
        raise HTTPException(status_code=404, detail='No results found')
    return results


@router.get('/get-claims/{search_str}')
def get_claims(search_str: str):
    results = utils.get_claims(search_str)
    if not results:
        raise HTTPException(status_code=404, detail='No results found')
    return results


@router.get('/get-page/{search_str}')
def get_page(search_str: str):
    return RedirectResponse(utils.get_entity(search_str)['url'])


@router.get('/get-scores')
def get_scores(types: list[str] = Query([]), answers: list[str] = Query([])):
    return finder.get_scores(types, answers)


@router.get('/get-answer')
def get_answer(types: list[str] = Query([]), answers: list[str] = Query([])):
    return finder.get_answer(types, answers)

@router.get('/get-answer-human')
def get_answer_human(types: list[str] = Query([]), answers: list[str] = Query([])):
    return finder.human_search(types, answers)
