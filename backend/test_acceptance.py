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

def test13():
    """Test searching ambiguous answers."""
    types = ['fruit']
    answers = ['apple', 'strawberry']
    correct_answer = 'apple'
    assert get_answer(types, answers) == correct_answer

def test14():
    """Test searching ambiguous answers."""
    types = ['actor']
    answers = ['Q212064', 'Q175535']
    correct_answer = 'Q212064'
    assert get_answer(types, answers) == correct_answer

def test15():
    """Test searching same type / answer."""
    types = ['Q11424']
    answers = ['Q11424', 'Q1420']
    correct_answer = 'Q11424'
    assert get_answer(types, answers) == correct_answer

def test16():
    """Second test searching same type as answer."""
    types = ['human']
    answers = ['fashion', 'human']
    correct_answer = 'human'
    assert get_answer(types, answers) == correct_answer

def test17():
    """Test searching one answer."""
    types = ['Q1075']
    answers = ['Q3142']
    correct_answer = 'Q3142'
    assert get_answer(types, answers) == correct_answer

def test18():
    """Test searching multiple of the same answer."""
    types = ['color']
    answers = ['orange', 'orange']
    correct_answer = 'orange'
    assert get_answer(types, answers) == correct_answer

def test19():
    """Normal test for type: film."""
    types = ['Q11424', 'Q16144339']
    answers = ['Q283', 'Q1420', 'Q26698156']
    correct_answer = 'Q26698156'
    assert get_answer(types, answers) == correct_answer

def test20():
    """Normal test for type: animal."""
    types = ['animal']
    answers = ['car', 'tiger', 'Q22676']
    correct_answer = 'tiger'
    assert get_answer(types, answers) == correct_answer

def test21():
    """Second test for animal type with car as possible answer."""
    types = ['animal']
    answers = ['car', 'elephant', 'building']
    correct_answer = 'elephant'
    assert get_answer(types, answers) == correct_answer

def test22():
    """Normal test for type: animal."""
    types = ['animal']
    answers = ['toy', 'lion', 'building']
    correct_answer = 'lion'
    assert get_answer(types, answers) == correct_answer

def test23():
    """Normal test for type: mammal."""
    types = ['mammal']
    answers = ['car', 'tiger', 'toy']
    correct_answer = 'tiger'
    assert get_answer(types, answers) == correct_answer

def test24():
    """Normal test searching human / country of citizenship"""
    types = ['human', 'Q30']
    answers = ['Q9673', 'Q8877', 'Q1426', 'Q8991894']
    correct_answer = 'Q8877'
    assert get_answer(types, answers) == correct_answer

def test25():
    """Normal test searching human"""
    types = ['human']
    answers = ['tiger', 'Q8877', 'car', 'ball']
    correct_answer = 'Q8877'
    assert get_answer(types, answers) == correct_answer

def test26():
    """Normal test searching human / language spoken"""
    types = ['human', 'Q36510']
    answers = ['Q8877', 'Q9673', 'Q1426', 'Q8991894']
    correct_answer = 'Q8991894'
    assert get_answer(types, answers) == correct_answer

def test27():
    """Normal test searching human / occupation"""
    types = ['Q10833314']
    answers = ['Q36159', 'Q1426', 'Q9673', 'tiger']
    correct_answer = 'Q1426'
    assert get_answer(types, answers) == correct_answer

def test28():
    """Normal test searching actor / film"""
    types = ['Q160071']
    answers = ['Q13909', 'Q36767', 'Q35332', 'Q3772']
    correct_answer = 'Q36767'
    assert get_answer(types, answers) == correct_answer

def test29():
    """Normal test searching human / president"""
    types = ['Q11696']
    answers = ['Q36767', 'Q22686', 'Q1426']
    correct_answer = 'Q22686'
    assert get_answer(types, answers) == correct_answer

def test30():
    """Normal test searching human / given name"""
    types = ['Q4925477']
    answers = ['Q155700', 'Q44437', 'Q313107']
    correct_answer = 'Q44437'
    assert get_answer(types, answers) == correct_answer

def test31():
    """Normal test searching human / billionaire"""
    types = ['Q1062083']
    answers = ['Q1426', 'Q590212', 'Q9673']
    correct_answer = 'Q590212'
    assert get_answer(types, answers) == correct_answer

def test32():
    """Normal test searching human (sex, first name, baseball team)"""
    types = ['human', 'male', 'Q18057751', 'Q5369']
    answers = ['Q1176561', 'Q448005', 'Q2852937', 'Q188792']
    correct_answer = 'Q448005'
    assert get_answer(types, answers) == correct_answer

def test33():
    """Normal test searching human (education, female)"""
    types = ['Q309350', 'Q6581072']
    answers = ['Q194280', 'Q16147452', 'Q6294']
    correct_answer = 'Q16147452'
    assert get_answer(types, answers) == correct_answer
