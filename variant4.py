import streamlit as st
import csv


def pas_list(data,ch):
    list=[]
    for line in data:
        if ch == "спасенные":
            if line[9] == '0' and line[1] == '1':
                list.append("Имя: " + line[3] + ", пол: " + line[4] + ", возраст: " + line[5])
        else:
            if line[9] == '0' and line[1] == '0':
                list.append("Имя: " + line[3] + ", пол: " + line[4] + ", возраст: " + line[5])
    return list


def variant4():
    ch = st.radio("Поиск пассажиров с билетом нулевой стоимости:", ["спасенные","погибшие"])
    with open('data.csv') as file:
        file_reader = csv.reader(file, delimiter=",")
        list=pas_list(file_reader,ch)
    st.subheader("Всего " + ch + " с билетами нулевой стоимости: " + str(len(list)))
    for lt in list:
        if ch == "спасенные":
            st.success(lt)
        else:
            st.error(lt)
