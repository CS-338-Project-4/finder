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
    animal_types = ['Q7377', 'Q152', 'Q5113', 'Q10908', 'Q1390']
    animal_names = ['mammal', 'insect', 'fish', 'bird', 'amphibian', 'reptile']
    #get dictionary of data for AnswerType
    if type_ids[0] == 'Q729':
        for i, answer in enumerate(answers): #for each answer in the list
            print(answer)
            claims = utils.get_claims(answer)
            print(claims.get('P1417'))

            if claims.get('P1417') is not None:
                scores[i] += 1
    elif type_ids[0] in animal_types:
        for i, answer in enumerate(answers): #for each answer in the list
            claims = utils.get_entity(answer)
            strings = claims['description'].split()
            for j in strings:
                if j == types[0]:
                    scores[i] += 1

    # type_search = True
    # while type_search:
    #     # for relation, entities in claims.items():
    #     # entity_ids = get_claim_ids(claims.values()) # entities
    #     #get all qNumbers for entities

    #     if claims.get('P1687') is None: #Wikidata Property, if there is no wikidata property, set claims to be the next instance (go up in the tree)
    #         claims = utils.get_claims(get_claim_ids(claims['P31'])[0])
    #     else: #if it does exists, get qNumber for the thing in property, and set it as type, break the while loop
    #         entity_ids = get_claim_ids(claims['P1687'])[0]
    #         #print (get_claim_ids(claims['P1687']), claims)
    #         type = entity_ids
    #         type_search = False

    #         # if relation.find("") == 'P1687': #Wikidata Property
    #         #     type = entity_ids[0]
    #         #     type_search = False
    #         #     break
    #         # elif relation == 'P31': #instance
    #         #     #next_instance = entities
    #         #     claims = utils.get_claims(entities[0])

    #     # entities_id = utils.get_ids(claims.values())
    #     # claims = utils.get_claims(entities_id)

    # for i, answer in enumerate(answers): #for each answer in the list
    #     claims = utils.get_claims(answer) #get the dictionary for answer
    #     if claims.get(type) is not None: #see if the type is in the dictionary
    #         entity_ids = get_claim_ids(claims[type]) #get the qNumbers for the entities in type
    #         for x in entity_ids:
    #             if x == type_ids[0]: #check if answer type is in entity_ids
    #                 scores[i] += 0
    #                 break
    #             else:
    #                 scores[i] += 1
    return scores

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
    relations_searched = (6, 17, 19, 21, 27, 30, 31, 35, 39, 50, 53, 54, 57,
                          58, 61, 69, 84, 86, 88, 91, 97, 98, 101, 102, 103,
                          106, 108, 110, 112, 115, 118, 123, 127, 131, 136,
                          137, 159, 161, 162, 169, 175, 176, 177, 178, 179,
                          206, 241, 276, 279, 287, 361, 413, 425, 452, 462,
                          463, 488, 495, 527, 611, 634, 641, 674, 706, 734,
                          735, 1412, 1552, 1830)
    p_relations = '|'.join((f'p:P{num}' for num in relations_searched))
    ps_relations = '|'.join((f'ps:P{num}' for num in relations_searched))

    scores = [0] * len(answers)
    type_ids = utils.get_ids(types)
    answer_ids = utils.get_ids(answers)

    def get_results(endpoint_url, query):
        user_agent = 'Finder/0.0 <darrylforbes2022@u.northwestern.edu>'
        sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()

    for i, answer_id in enumerate(answer_ids):
        for type_id in type_ids:
            if answer_id == type_id:
                scores[i] += 1
                continue
            try:
                relation_query = (
                    'SELECT ?item ?relationP '
                    'WHERE { '
                    f'wd:{answer_id} ({p_relations})? ?st . '  # Narrows down relations
                    f'wd:{answer_id} ?relationP ?st . '
                    '?st ?relationPS ?item . '
                    f'?st ({ps_relations})? ?item . '  # Narrows down relations
                    f'?item wdt:P31?/wdt:P279?/wdt:P279? wd:{type_id} . '
                    'FILTER( STRSTARTS( STR(?relationPS), "http://www.wikidata.org/prop/statement/" ) ) . '
                    '} group by ?item ?relationP '
                    'LIMIT 1000'
                )

                results = get_results(endpoint_url, relation_query)['results']['bindings']
                if results:
                    label_id = results[0]['relationP']['value'].split('/')[-1]
                    items = {r['item']['value'].split('/')[-1] for r in results}
                    claims = utils.get_claims(answer_id)
                    if claims.get(label_id):  # See if the type is in the dictionary
                        entity_ids = get_claim_ids(claims[label_id])  # Get the qNumbers for the entities in type
                        scores[i] += 1
                        for entity in entity_ids:
                            if entity in items:
                                scores[i] += 0
                                break
                            scores[i] -= round(1/len(entity_ids), 2)
            except:
                print(f'Query timed out - {answer_id}, {type_id}')


    claims = utils.get_claims(type_ids)
    animal_types = ['Q7377', 'Q152', 'Q5113', 'Q10908', 'Q1390', 'Q10811']
    animal_names = ['mammal', 'insect', 'fish', 'bird', 'amphibian', 'reptile']
    types = utils.get_entity(type_ids[0])['label']
    #get dictionary of data for AnswerType
    if type_ids[0] == 'Q729':
        for i, answer in enumerate(answers): #for each answer in the list
            claims = utils.get_claims(answer)
            if claims.get('P1417'):
                if claims.get('P1417')[0]['mainsnak']['datavalue']['value'].split('/')[0] == 'animal':
                    scores[i] += 1
    elif type_ids[0] in animal_types:
        for i, answer in enumerate(answers): #for each answer in the list
            claims = utils.get_entity(answer)
            strings = claims['description'].split()
            for j in strings:
                if j == types:
                    scores[i] += 1
    return scores
