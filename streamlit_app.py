import streamlit as st
import pandas as pd
import time
import os, sys
def get_user_name():
    return 'John'

st.header(os.getenv("QUERY_STRING"))
