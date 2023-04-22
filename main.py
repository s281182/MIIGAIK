import streamlit as st
import variant1.py
#import var2.ry
#import var3.ry
#import var4.ry

def user_name(par):
    if par=="var1":
        return "Вариант 1, выполнил Горелкин А."
    elif par=="var2":
        return "Вариант 2, выполнила Гочияева Л."
    elif par=="var3":
        return "Вариант 3, выполнила Исмагилова Э."
    elif par=="var4":
        return "Вариант 4, выполнил Бутов С."


st.title("Команда №4, практическая работа 10")
var=st.selectbox(
    label="Выбери вариант:",
    options=["var1","var2","var3","var4"],
    format_func=user_name
)

if var == "var1":
    st.text("Вариант 1, выполнил Горелкин А.")
    variant1()
elif var == "var2":
    st.text("Вариант 2, выполнила Гочияева Л.")
    #var2()
elif var == "var3":
    st.text("Вариант 3, выполнила Исмагилова Э.")
    #var3()
elif var == "var4":
    st.text("Вариант 4, выполнил Бутов С.")
    #var4()
