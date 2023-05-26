import streamlit as st
import pandas as pd
import csv
from Evgeny import *
from Kate import *
from Evgeny_Test import *
from Alina import *
from Vadim import *

st.title('STREAMLIT PROJECT КОМАНДЫ 2022-ФГиИБ-ПИ-2см')
st.divider()
st.subheader('Выберите нужный вариант: ')

select = st.radio('Выберите исполнителя:', ['Екатерина', 'Алина', 'Вадим', 'Евгений'])
if select == 'Екатерина':
    male_saved, male_dead, female_saved, female_dead = get_result(data)
    test_saved_male()
    test_saved_female()
    test_dead_male()
    test_dead_female()
    #Программа для Стримлит на основе полученных данных
    st.title('Спасенные и погибшие на Титанике')
    st.header('Вариант 8 (Ленская Е.И. группа ПИ-2см)')
    st.subheader('Посчитать количество пассажиров (выбрав пол, и спасенных или погибших)')
choice = st.radio('Укажите пол:', ['муж', 'жен'])
if choice == 'муж':
    choice = st.radio('Спасен или погиб:', ['спасен', 'погиб'])
    if choice == 'спасен':
        st.success(f"Количество спасенных мужчин - {male_saved}")
    else:
        st.error(f"Количество погибших мужчин - {male_dead}")
else:
    choice = st.radio('Спасен или погиб:', ['спасен', 'погиб'])
    if choice == 'спасен':
        st.success(f"Количество спасенных женщин - {female_saved}")
    else:
        st.error(f"Количество погибших женщин - {female_dead}")
if select == 'Алина':
    test_fare()
    Alina_Function()
if select == 'Вадим':
    Vadim_Function()
if select == 'Евгений':
    Testing_Function_1()
    Testing_Function_2()
    Testing_Function_3()
    Evgeny_Function()

