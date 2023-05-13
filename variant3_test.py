from variant3 import get_pass_list


def test_pass_list_all():
    data = ['9,1,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27',
            '5,1,3,"Allen, Mr. William Henry",male,35', '25,1,3,"Palsson, Miss. Torborg Danira",female,8']
    assert get_pass_list(data, '') == ['3, "Johnson  Mrs. Oscar W (Elisabeth Vilhelmina Berg)", 27',
                                       '3, "Allen  Mr. William Henry", 35', '3, "Palsson  Miss. Torborg Danira", 8']


def test_pass_list_name():
    data = ['9,1,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27',
            '5,1,3,"Allen, Mr. William Henry",male,35', '25,1,3,"Palsson, Miss. Torborg Danira",female,8']
    assert get_pass_list(data, 'John') == ['3, "Johnson  Mrs. Oscar W (Elisabeth Vilhelmina Berg)", 27']
