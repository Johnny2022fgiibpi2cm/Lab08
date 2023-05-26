import streamlit as st
import pandas as pd
import csv
from Evgeny import *
from Evgeny_Test import *
from Kate import *
from Alina import *
from Vadim import *

st.title('STREAMLIT PROJECT КОМАНДЫ 2022-ФГиИБ-ПИ-2см')
st.divider()
st.subheader('Выберите нужный вариант: ')

select = st.radio('Выберите исполнителя:', ['Екатерина', 'Алина', 'Вадим', 'Евгений'])
if select == 'Екатерина':
    Kate_Function()
if select == 'Алина':
    Alina_Function()
if select == 'Вадим':
    Vadim_Function()
if select == 'Евгений':
    Testing_Function_1()
    Testing_Function_2()
    Testing_Function_3()
    Evgeny_Function()

