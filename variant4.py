import streamlit as st


def pas_list(data,ch):
    list=[]
    for line in data:
        lst = line.rstrip().split(",")
        if ch == "спасенные":
            if lst[10] == '0' and lst[1] == '1':
                list.append("Имя: " + lst[3] + " " + lst[4] + ", пол: " + lst[5] + ", возраст: " + lst[6])
        else:
            if lst[10] == '0' and lst[1] == '0':
                list.append("Имя: " + lst[3] + " " + lst[4] + ", пол: " + lst[5] + ", возраст: " + lst[6])
    return list


def variant4():
    ch = st.radio("Поиск пассажиров с билетом нулевой стоимости:", ["спасенные","погибшие"])
    with open('data.csv') as file:
        data = file.readlines()[1:]
    list=pas_list(data,ch)
    st.subheader("Всего " + ch + " с билетами нулевой стоимости: " + str(len(list)))
    for lt in list:
        if ch == "спасенные":
            st.success(lt)
        else:
            st.error(lt)
