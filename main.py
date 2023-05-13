import streamlit as st
import csv
import variant1
import variant2
import variant3
import variant4


def user_name(par):
    if par == "var1":
        return "Вариант 1"
    elif par == "var2":
        return "Вариант 2"
    elif par == "var3":
        return "Вариант 3"
    elif par == "var4":
        return "Вариант 4"

st.set_page_config(layout="wide")
st.title("Команда №4, практическая работа 10")
st.markdown("Вариант1: Выводит долю пассажиров среди погибших или выживших в возрастных группах «до 30 лет» или «старше 60». (Автор Горелкин А.)  \n"
            "Вариант2: Выводит долю выживших среди пассажиров указанного пола. (Автор Гочияева Л.)  \n"
            "Вариант3: Выводит классы билетов, имена и возраст спасенных пассажиров с указанными именами. (Автор Исмагилова Э.)  \n"
            "Вариант4: Выводит список пассажиров среди спасенных или погибших с билетами нулевой стоимости. (Автор Бутов С.)")
var=st.selectbox(
    label="Выберите интересующий Вас вариант:",
    options=["var1","var2","var3","var4"],
    format_func=user_name
)
st.text(user_name(var))
if var == "var1":
    variant1.variant1()
elif var == "var2":
    variant2.variant2()
elif var == "var3":
    variant3.variant3()
elif var == "var4":
    variant4.variant4()
