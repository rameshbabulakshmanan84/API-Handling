import pandas as pd
import streamlit as st
#print("This is new")

st.title("Welcome to Streamlit")

checkbox_one = st.checkbox("yes")

checkbox_two = st.checkbox("No")

if checkbox_one:
    value="yes"
elif checkbox_two:
    value="No"
else:
    value="No Value selected"


texbox= st.text_input


selectbox  = st.selectbox(

"Select Yes or No",["Yes","No"]

)

st.write(f'You selected {selectbox}')

st.write(f'you selected {texbox}')

dic = {'name':'Ramesh','age':36}

st.write(dic)