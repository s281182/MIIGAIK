import streamlit as st


def get_pass_list(data, name):
    out_list = []
    for line in data:
        lst = line.rstrip().split(",")
        if lst[1] == "1" and str(lst[3] + ' ' + lst[4])[1:-1].startswith(name):
            out_list += [lst[2]+', '+lst[3]+' '+lst[4]+', '+lst[6]]
    return out_list


def variant3():
    with open("data.csv") as file:
        data = file.readlines()
    name = st.text_input("Введите имя спасенного пассажира:")
    st.table({"Данные спасенного пассажира(класс билета, имя, возраст):": get_pass_list(data, name)})


variant3()
