import streamlit as st
import csv

#Функция не зависит от файла Титаник
def get_result(data):
    male_saved = 0
    male_dead = 0
    female_saved = 0
    female_dead = 0
    for line in data:
        if line.split(',')[5] == 'male':
            if line.split(',')[1] == '1':
                male_saved += 1
            else:
                male_dead += 1
        elif line.split(',')[5] == 'female':
            if line.split(',')[1] == '1':
                female_saved += 1
            else:
                female_dead += 1
    return male_saved, male_dead, female_saved, female_dead

#Вывели файл Титаник из функции
with open('data.csv') as file:
    data = file.readlines()

male_saved, male_dead, female_saved, female_dead = get_result(data)
#print(male_saved, male_dead, female_saved, female_dead)



