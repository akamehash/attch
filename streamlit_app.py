import streamlit as st
import os, sys

GET={}
args=os.getenv("QUERY_STRING").split('&')

for arg in args: 
    t=arg.split('=')
    if len(t)>1: k,v=arg.split('='); GET[k]=v

my_placeholder = st.empty()
my_placeholder.text("The user entered %s" + GET.get('user_id') +'<br><form action="" method="POST"><input type="text" name="username"><input type="submit" value="Submit"></form> ')

