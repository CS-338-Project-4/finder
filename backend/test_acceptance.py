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
    answers = ['kraken', 'Minotaur', 'Giant', 'Q15721']
    correct_answer = 'Q15721'
    assert get_answer(types, answers) == correct_answer


def test7():
    """Test two answers."""
    types = ['programming language']
    answers = ['python', 'water']
    correct_answer = 'python'
    assert get_answer(types, answers) == correct_answer


def test8():
    """Test two types."""
    types = ['programming language', 'scripting language']
    answers = ['java', 'python', 'false']
    correct_answer = 'python'
    assert get_answer(types, answers) == correct_answer


def test9():
    """Test searching unique IDs."""
    types = ['business']
    answers = ['Q89', 'Q312']
    correct_answer = 'Q312'
    assert get_answer(types, answers) == correct_answer


def test10():
    """Test searching unique IDs."""
    types = ['enterprise', 'business', 'fruit']
    answers = ['Q89', 'Q312']
    correct_answer = 'Q312'
    assert get_answer(types, answers) == correct_answer


def test11():
    """Test ranking issue in relation query (Tom Cruise bug)."""
    types = ['actor']
    answers = ['Steven Spielberg', 'Tom Cruise']
    correct_answer = 'Tom Cruise'
    assert get_answer(types, answers) == correct_answer


def test12():
    """Test discovered bug in relation query score calculation."""
    types = ['lawyer', 'film director', 'film producer', 'actor']
    answers = ['Barack Obama', 'Steven Spielberg']
    correct_answer = 'Steven Spielberg'
    assert get_answer(types, answers) == correct_answer
