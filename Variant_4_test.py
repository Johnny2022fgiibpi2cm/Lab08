import streamlit as st
from Variant_4 import get_fare

def test_fare():
 data = ['0,1,2,.Грейнджер, Гермиона.,5,6,7,8,9,56', '0,1,2,/Поттер, Гарри.,5,6,7,8,9,5', '0,1,2,-Уизли, Рон.,5,6,7,8,9,31']
 assert get_fare(data) == ['Грейнджер Гермиона']




