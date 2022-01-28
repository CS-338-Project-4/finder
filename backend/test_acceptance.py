from finder import get_answer


def test0():
    types = ['programming language']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'python'
    assert get_answer(types, answers) == correct_answer


def test1():
    types = ['environmental resource']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'water'
    assert get_answer(types, answers) == correct_answer


def test2():
    """Test two levels up in ontology."""
    types = ['tool']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'scissors'
    assert get_answer(types, answers) == correct_answer


def test3():
    types = ['truth value']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'false'
    assert get_answer(types, answers) == correct_answer


def test4():
    types = ['film director']
    answers = ['John Krasinski', 'Jack Black', 'Steven Spielberg', 'Barack Obama']
    correct_answer = 'Steven Spielberg'
    assert get_answer(types, answers) == correct_answer


def test5():
    types = ['water deity']
    answers = ['Hades', 'Poseidon', 'Zeus', 'Hera']
    correct_answer = 'Poseidon'
    assert get_answer(types, answers) == correct_answer


def test6():
    types = ['mythological serpent']
    answers = ['kraken', 'Minotaur', 'Giant', 'Python']
    correct_answer = 'Python'
    assert get_answer(types, answers) == correct_answer
