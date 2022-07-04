import streamlit as st

code = ''' <html>
    <body>
        <title>Hello World</title>
        <meta charset="UTF-8">
   </body>
   <head>
   <form action="" method="get"><input type="text" name="username"><input type="submit" value="Submit"></form><br>
        <h1>Hello Example!</h1>
        <br>
        <p>Hello world</p>
    </head>
</html>'''
st.code(code,language='html')

with st.echo():
