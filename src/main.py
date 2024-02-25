from langchainhelper import get_chain
import streamlit as st
import os
from get_vector_db import get_vector__db


csv_file_path = '/Users/omdeshmukh/Downloads/SemVI/FAQ-Assistant/data/demo.csv'
db_path =  os.path.split(csv_file_path)[0]+'/vector_db'

st.title("FAQ-Assistant")

btn = st.button("Create Database")

if btn:
    db_path = get_vector__db(csv_file_path=csv_file_path)
    
chain = get_chain(db_path)
question = st.text_input("Question: ")
if(question):
    answer = chain(question)
    st.header("Answer:")
    st.write(answer['result'])


