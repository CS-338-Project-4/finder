import utils


def get_answer(types: list[str], answers: list[str]) -> str:
    """Return answer with highest score."""
    scores = get_scores(types, answers)
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
