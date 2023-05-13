from variant4 import pas_list


def test_saved_free():
    data = ['0,1,2,3,4,5,6,7,8,9,0', '0,1,2,3,4,5,6,7,8,9,1', '0,1,2,3,4,5,6,7,8,9,0']
    assert pas_list(data, "спасенные") == ['Имя: 3 4, пол: 5, возраст: 6', 'Имя: 3 4, пол: 5, возраст: 6']


def test_unsaved_free():
    data = ['0,0,2,3,4,5,6,7,8,9,0', '0,0,2,3,4,5,6,7,8,9,1', '0,0,2,3,4,5,6,7,8,9,0']
    assert pas_list(data, "погибшие") == ['Имя: 3 4, пол: 5, возраст: 6', 'Имя: 3 4, пол: 5, возраст: 6']


def test_saved_paid():
    data = ['0,1,2,3,4,5,6,7,8,9,1', '0,1,2,3,4,5,6,7,8,9,1', '0,1,2,3,4,5,6,7,8,9,1']
    assert pas_list(data, "спасенные") == []


def test_unsaved_paid():
    data = ['0,1,2,3,4,5,6,7,8,9,1', '0,1,2,3,4,5,6,7,8,9,1', '0,1,2,3,4,5,6,7,8,9,1']
    assert pas_list(data, "погибшие") == []


def test_saved_free_count():
    data = ['0,1,2,3,4,5,6,7,8,9,0', '0,1,2,3,4,5,6,7,8,9,1', '0,1,2,3,4,5,6,7,8,9,0']
    assert len(pas_list(data, "спасенные")) == 2


def test_saved_unsaved_count():
    data = ['0,0,2,3,4,5,6,7,8,9,0', '0,0,2,3,4,5,6,7,8,9,0', '0,0,2,3,4,5,6,7,8,9,0']
    assert len(pas_list(data, "погибшие")) == 3
