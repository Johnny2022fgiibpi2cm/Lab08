import streamlit as st
import pandas as pd
import csv
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
    Evgeny_Function()

