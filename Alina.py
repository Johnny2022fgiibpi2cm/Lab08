import streamlit as st

def Alina_Function():
 st.title('Титаник')
 st.header('Вариант 4 (Елисеева А.А. группа ПИ-2см)')
 st.subheader('Вывести имена пассажиров, стоимость билета которых была выше указанной')
 choice = st.number_input('Укажите стоимость билета')
 if st.button('Показать'):
    with open("C:\\Users\\Администратор\\Desktop\\Lab9\\data.csv") as file:
     for line in file:
         if line.split(",")[10] != 'Cabin':
             fare = float(line.split(",")[10])
             name = line.split(",")[3] + line.split(",")[4]
             if fare >= choice:
               st.text(f"{name[1:-1]}{fare}")




