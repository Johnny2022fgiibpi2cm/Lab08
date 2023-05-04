import streamlit as st
import csv

def Kate_Function():
 male_saved = 0
 male_dead = 0
 female_saved = 0
 female_dead = 0

 with open('data.csv') as f:
     reader = csv.DictReader(f)
     for line in reader:
         if line['Sex'] == 'male':
             if line['Survived'] == '1':
                 male_saved += 1
             else:
                 male_dead += 1
         elif line['Sex'] == 'female':
             if line['Survived'] == '1':
                 female_saved += 1
             else:
                 female_dead += 1

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












