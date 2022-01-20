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
    types = ['boolean']
    answers = ['python', 'water', 'scissors', 'false']
    correct_answer = 'false'
    assert get_best_answer(types, answers) == correct_answer
