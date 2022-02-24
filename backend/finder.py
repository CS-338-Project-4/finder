import utils
import sys
from itertools import product
from SPARQLWrapper import SPARQLWrapper, JSON


def get_answer(types: list[str], answers: list[str]) -> str:
    """Return answer with highest score."""
    # scores = get_scores(types, answers)
    scores = get_sparql(types, answers)
    return answers[scores.index(max(scores))]


def get_scores(types: list[str], answers: list[str]) -> list[int]:
    """Return scores for all answers."""
    if not (types and answers):
        raise ValueError

    type_ids = utils.get_ids(types)
    # print('\n\n', type_ids)

    scores = [0] * len(answers)

    for i, answer in enumerate(answers):
        claims = utils.get_claims(answer)
        # print('relations:', claims.keys())
        for relation, entities in claims.items():
            entity_ids = get_claim_ids(entities)
            if relation == 'P31':  # Instance of
                # print(answer, '- Instance of:', utils.get_labels(entity_ids))
                # print(entity_ids)
                scores[i] += search_tree(type_ids, entity_ids, 2)
            elif relation == 'P279':  # Subclass of
                # print(answer, 'Subclass of:', utils.get_labels(entity_ids))
                # print(entity_ids)
                scores[i] += search_tree(type_ids, entity_ids, 2)
            scores[i] += sum(x in entity_ids for x in type_ids)

    return scores


def human_search(types: list[str], answers: list[str])-> str:
    if not (types and answers):
        raise ValueError

    type_ids = utils.get_ids(types)
    #get the qNumber of AnswerType
    # print('\n\n', type_ids)

    scores = [0] * len(answers)
    claims = utils.get_claims(type_ids)
    #get dictionary of data for AnswerType

    type_search = True
    while type_search:
        # for relation, entities in claims.items():
        # entity_ids = get_claim_ids(claims.values()) # entities
        #get all qNumbers for entities

        if claims.get('P1687') is None: #Wikidata Property, if there is no wikidata property, set claims to be the next instance (go up in the tree)
            claims = utils.get_claims(get_claim_ids(claims['P31'])[0])
        else: #if it does exists, get qNumber for the thing in property, and set it as type, break the while loop
            entity_ids = get_claim_ids(claims['P1687'])[0]
            #print (get_claim_ids(claims['P1687']), claims)
            type = entity_ids
            type_search = False

            # if relation.find("") == 'P1687': #Wikidata Property
            #     type = entity_ids[0]
            #     type_search = False
            #     break
            # elif relation == 'P31': #instance
            #     #next_instance = entities
            #     claims = utils.get_claims(entities[0])

        # entities_id = utils.get_ids(claims.values())
        # claims = utils.get_claims(entities_id)

    for i, answer in enumerate(answers): #for each answer in the list
        claims = utils.get_claims(answer) #get the dictionary for answer
        if claims.get(type) is not None: #see if the type is in the dictionary
            entity_ids = get_claim_ids(claims[type]) #get the qNumbers for the entities in type
            print(entity_ids)
            for x in entity_ids:
                if x == type_ids[0]: #check if answer type is in entity_ids
                    scores[i] += 0
                    print(x, type_ids[0])
                    break
                else:
                    scores[i] += 1
                    print(x, type_ids[0])
    print(scores)
    return answers[scores.index(min(scores))]

def search_tree(type_ids: list[str], answer_ids: list[str],
                depth_limit: int) -> int:
    if not (type_ids and answer_ids):
        raise ValueError
    elif depth_limit == 0:
        return 0

    score = 0

    for answer in answer_ids:
        claims = dict(utils.get_claims(answer, 'P31'),
                      **utils.get_claims(answer, 'P279'))
        for relation, entities in claims.items():
            entity_ids = get_claim_ids(entities)
            if relation == 'P31':  # Instance of
                # print(utils.get_labels([answer])[0], '- Instance of:', utils.get_labels(entity_ids))
                score += search_tree(type_ids, entity_ids, depth_limit - 1)
            elif relation == 'P279':  # Subclass of
                # print(utils.get_labels([answer])[0], 'Subclass of:', utils.get_labels(entity_ids))
                score += search_tree(type_ids, entity_ids, depth_limit - 1)
            score += sum(x in entity_ids for x in type_ids)

    return score


def get_claim_ids(entities: dict) -> list['str']:
    """Return the IDs that exist in a given claim/relation."""
    entity_ids = []
    for e in entities:
        try:
            entity_ids.append(e['mainsnak']['datavalue']['value']['id'])
        except:
            pass

    return entity_ids


def get_sparql(types: list[str], answers: list[str]) -> list[int]:
    endpoint_url = "https://query.wikidata.org/sparql"

    scores = [0] * len(answers)
    type_ids = utils.get_ids(types)
    answer_ids = utils.get_ids(answers)

    def get_results(endpoint_url, query):
        user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
        # TODO adjust user agent; see https://w.wiki/CX6
        sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()

    for i, answer_id in enumerate(answer_ids):
        for type_id in type_ids:
            relation_query = (
                'SELECT ?relationP ?relationPLabel (count (*) as ?count)'
                'WHERE {'
                f'?answerDescendant wdt:P31?/wdt:P279* wd:{answer_id} .'
                '?answerDescendant ?relationP ?statement.'
                f'?statement ?relationPS wd:{type_id} .'
                'FILTER( STRSTARTS( STR(?relationPS), "http://www.wikidata.org/prop/statement/" ) ) .'
                'SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }'
                '} group by ?relationP ?relationPLabel order by desc(?count)'
            )
            results = get_results(endpoint_url, relation_query)['results']['bindings']
            if results:
                label = results[0]['relationP']['value']
                label_id = label.split('/')[-1]
                claims = utils.get_claims(answer_id)
                if claims.get(label_id) is not None: #see if the type is in the dictionary
                    entity_ids = get_claim_ids(claims[label_id]) #get the qNumbers for the entities in type
                    scores[i] += 1
                    length = len(entity_ids)
                    go_next = True
                    for x in entity_ids:
                        if x == type_id: #check if answer type is in entity_ids
                            scores[i] += 0
                            go_next = False
                        elif go_next:
                            scores[i] -= round(1/length, 2)

            tree_query = (
                'SELECT ?item ?itemLabel'
                'WHERE {'
                f'wd:{answer_id} (p:P31?|p:P279) ?st .'
                '?st (ps:P31?|ps:P279) ?item .'
                f'?item wdt:P31?/wdt:P279* wd:{type_id} .'
                'SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }'
                '}'
            )

            results = get_results(endpoint_url, tree_query)['results']['bindings']
            scores[i] += len(results)

    return scores
