import streamlit as st
import pandas as pd
import csv
import time

def Evgeny_Function():
 df = {}
 List = ''
 warning = ''
 titanic_data_1 = {}
 titanic_data_2 = {}
 titanic_data_3 = {}
 titanic_data_4 = {}

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
             count = 0
             count2 = 1

         with open('data.csv', encoding='utf-8') as result_file:
             file_reader = csv.reader(result_file, delimiter = ",")
             for row in file_reader:
                 if row[1] == '1' and row[2] in add_multiselect1 and row[4] in add_multiselect2:
                     titanic_data_4[count2] = str(f'{row[2]}')
                     titanic_data_1[count2] = str(f'{row[3]}')
                     titanic_data_2[count2] = str(f'{row[4]}')
                     titanic_data_3[count2] = str(f'{row[5]}')
                     count2 += 1
             count += 1
 else:
     data = pd.read_csv('data.csv')
     st.write(data)

 df = pd.DataFrame({
         "Pclass": titanic_data_4,
         "Name": titanic_data_1,
         "Sex": titanic_data_2,
         "Age": titanic_data_3, 
     })
 st.dataframe(df)
