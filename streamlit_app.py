import streamlit as st
import os, sys

my_placeholder = st.empty()
my_placeholder.text("The user entered %s" % os.getenv("QUERY_STRING") +'<br><form action="" method="get"><input type="text" name="username"><input type="submit" value="Submit"></form> ')

