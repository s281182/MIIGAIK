from variant2 import get_result

def test_variant2_male():
    data = ['0,2,2,3,4,male', '0,2,2,3,4,male', '0,1,2,3,4,male', '0,2,2,3,4,female', '0,1,2,3,4,male']
    assert get_result(data, 'муж') == 0.5

def test_variant2_female():
    data = ['0,1,2,3,4,male', '0,1,2,3,4,male', '0,1,2,3,4,male', '0,2,2,3,4,female', '0,1,2,3,4,male']
    assert get_result(data, 'жен') == 0