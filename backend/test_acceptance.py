from finder import get_best_answer


def test0():
    types = ['programming languages']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'python'
    assert get_best_answer(types, answers) == correct_answer


def test1():
    types = ['liquid']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'water'
    assert get_best_answer(types, answers) == correct_answer


def test2():
    types = ['tool']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'scissors'
    assert get_best_answer(types, answers) == correct_answer


def test3():
    types = ['truth value']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'false'
    assert get_best_answer(types, answers) == correct_answer


def test4():
    types = ['film director']
    answers = ['Steven Spielberg', 'John Krasinski', 'Jack Black', 'Barack Obama']
    correct_answer = 'Steven Spielberg'
    assert get_best_answer(types, answers) == correct_answer


def test5():
    types = ['water deity']
    answers = ['Poseidon', 'Hades', 'Zeus', 'Hera']
    correct_answer = 'Poseidon'
    assert get_best_answer(types, answers) == correct_answer


def test6():
    types = ['mythological serpent']
    answers = ['Python', 'kraken', 'Minotaur', 'Giant']
    correct_answer = 'Python'
    assert get_best_answer(types, answers) == correct_answer
