import utils
from SPARQLWrapper import SPARQLWrapper, JSON


def get_answer(types: list[str], answers: list[str]) -> str:
    """Return answer with highest score."""
    scores = get_sparql(types, answers)
    return answers[scores.index(max(scores))]


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
