import streamlit as st


def get_result(data, sex):
    if sex == 'муж':
        sex = 'male'
    else:
        sex = 'female'
    all_sex = 0
    survived = 0
    for line in data:
        lst = line.rstrip().split(",")
        if lst[5] == sex:
            all_sex += 1
        if lst[1] == "1" and lst[5] == sex:
            survived += 1
    return round(survived / all_sex, 2)


def variant2():
    with open("data.csv") as file:
        data = file.readlines()

    sex = st.radio('Выберите пол спасенных пассажиров:', ['муж', 'жен'])
    if sex == 'муж':
        s = 'мужчин'
    else:
        s = 'женщин'
    st.text(f'Доля выживших среди {s}: {get_result(data, sex)}')
