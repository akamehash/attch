import streamlit as st
import cgi
form = cgi.FieldStorage()

my_placeholder = st.empty()
my_placeholder.text("The user entered %s" % form.getvalue("uservalue") +'<br><form action="" method="get"><input type="text" name="username"><input type="submit" value="Submit"></form> ')

