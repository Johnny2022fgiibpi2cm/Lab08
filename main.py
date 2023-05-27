import streamlit as st
import pandas as pd
import csv
import time
from Variant_6 import *
from Variant_6_test import *
from Variant_8_ import *
from Variant_8_test_ import *
from Variant_4_ import *
from Variant_4_test_ import *

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
    st.title('Титаник')
    st.header('Вариант 4 (Елисеева А.А. группа ПИ-2см)')
    st.subheader('Вывести имена пассажиров, стоимость билета которых была выше указанной')
    choice = st.number_input('Укажите стоимость билета')
    if st.button('Показать'):
       with open("data.csv") as file:
        for line in file:
            if line.split(",")[10] != 'Cabin':
                fare = float(line.split(",")[10])
                name = line.split(",")[3] + line.split(",")[4]
                if fare >= choice:
                  st.text(f"{name[1:-1]}{fare}")
if select == 'Вадим':
    st.subheader('Мой модуль еще в разработке...')
if select == 'Евгений':
    with open('data.csv') as file:
        data_file = file.readlines()

    df = {}
    List_Pclass = []; List_Name = []; List_Sex = []; List_Age = []
    warning = ''

    st.title('Hey, it is my project TITANIC')
    st.divider()
    st.subheader('My name: Evgeny. My group: 2022-FGiIB-PI-2SM ')
    st.success('Вариант-6. Вывести Name, Sex, Age спасенных пассижиров указанного класса и пола.')

    with st.sidebar:
        add_multiselect1 = st.multiselect(
            'Выберите класс пассажира',
            ['1', '2', '3'])

    with st.sidebar:
        add_multiselect2 = st.multiselect(
            'Выберите пол пассажира',
            ['male', 'female'])
        add_button = st.button('показать')

    if add_button:
        if not add_multiselect1 or not add_multiselect2:
            st.error('Заданы не все данные условия!')
        else:
            with st.spinner('Загрузка...'):
                time.sleep(5)
                st.success('Данные загружены!')

            for row in data_file:
                if row.split(",")[1] == '1' and row.split(",")[2] in add_multiselect1 and row.split(",")[5] in add_multiselect2:
                    List_Pclass.append(row.split(",")[2])
                    List_Name.append(row.split(",")[3] + row.split(",")[4] )
                    List_Sex.append(row.split(",")[5])
                    List_Age.append(row.split(",")[6])
    else:
        data = pd.read_csv('data.csv')
        st.write(data)

    df = pd.DataFrame({
            "Pclass": List_Pclass,
            "Name": List_Name,
            "Sex": List_Sex,
            "Age": List_Age
      })
    st.dataframe(df)
    Testing_Function_1()
    Testing_Function_2()
    Testing_Function_3()

