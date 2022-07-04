import streamlit as st
import cgi
form = cgi.FieldStorage()
st.header(form["username"])

my_placeholder = st.empty()
my_placeholder.text('<form action="" method="get"><input type="text" name="username"><input type="submit" value="Submit"></form> ')

