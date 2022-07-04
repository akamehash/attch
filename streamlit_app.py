import streamlit as st

code = ''' <html>
    <body>
        <title>Hello World</title>
        <meta charset="UTF-8">
   </body>
   <head>

        <h1>Hello Example!</h1>
        <br>
        <p>Hello world</p>
    </head>
</html>'''
st.code(code,language='html')

with st.echo():
