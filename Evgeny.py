import streamlit as st
import pandas as pd
import csv
import time

with open('data.csv') as file:
    data_file = file.readlines()

def Evgeny_Function():
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
