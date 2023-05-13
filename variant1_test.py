from variant1 import calculate_dataframe_stats

# age < 30, > 60, empty age -- max alike
input1 = [
    # ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    ['10', '0', '3', 'Hansen, Mr. Claus Peter', 'male', '41', '2', '0', '350026', '14.1083', '', 'S'],
    ['11', '0', '2', 'Giles, Mr. Frederick Edward', 'male', '21', '1', '0', '28134', '11.5', '', 'S'],
    ['12', '1', '1', 'Swift, Mrs. Frederick Joel (Margaret Welles Barron)', 'female', '48', '0', '0', '17466', '25.9292', 'D17', 'S'],
    ['13', '0', '3', 'Sage, Miss. Dorothy Edith "Dolly"', 'female', '', '8', '2', 'CA. 2343', '69.55', '', 'S'],
    ['14', '0', '2', 'Gill, Mr. John William', 'male', '24', '0', '0', '233866', '13', '', 'S'],
    ['15', '1', '2', 'Bystrom, Mrs. (Karolina)', 'female', '42', '0', '0', '236852', '13', '', 'S'],
    ['253', '0', '1', 'Stead, Mr. William Thomas', 'male', '62', '0', '0', '113514', '26.55', 'C87', 'S']
]

output1 = (0, 0, 29, 14)

# empty frame
input2 = [
]

output2 = (0, 0, 0, 0)

# age beetwin [30, 60] range
input3 = [
    ['10', '0', '3', 'Hansen, Mr. Claus Peter', 'male', '41', '2', '0', '350026', '14.1083', '', 'S'],
    ['12', '1', '1', 'Swift, Mrs. Frederick Joel (Margaret Welles Barron)', 'female', '48', '0', '0', '17466', '25.9292', 'D17', 'S'],
    ['15', '1', '2', 'Bystrom, Mrs. (Karolina)', 'female', '42', '0', '0', '236852', '13', '', 'S'],
]

output3 = (0, 0, 0, 0)

# age < 30 only
input4 = [
    ['11', '0', '2', 'Giles, Mr. Frederick Edward', 'male', '21', '1', '0', '28134', '11.5', '', 'S'],
    ['14', '0', '2', 'Gill, Mr. John William', 'male', '24', '0', '0', '233866', '13', '', 'S'],
]

output4 = (0, 0, 100, 0)

# age > 60 only
input5 = [
    ['253', '0', '1', 'Stead, Mr. William Thomas', 'male', '62', '0', '0', '113514', '26.55', 'C87', 'S']
]

output5 = (0, 0, 0, 100)

# no age entry only
input6 = [
    ['13', '0', '3', 'Sage, Miss. Dorothy Edith "Dolly"', 'female', '', '8', '2', 'CA. 2343', '69.55', '', 'S'],
]

output6 = (0, 0, 0, 0)

def test1():
    assert calculate_dataframe_stats(input1) == output1

def test2():
    assert calculate_dataframe_stats(input2) == output2

def test3():
    assert calculate_dataframe_stats(input3) == output3

def test4():
    assert calculate_dataframe_stats(input4) == output4

def test5():
    assert calculate_dataframe_stats(input5) == output5

def test6():
    assert calculate_dataframe_stats(input6) == output6
