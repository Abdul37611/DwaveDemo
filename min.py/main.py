
import streamlit as st
import numpy as np 
import pandas as pd
import streamlit.components.v1 as components



components.html(
"""
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <header>
        Embedding HTML file in streamlit
    </header>
    <footer>
        sample
    </footer>
</body>
</html>
"""
)

html=open("main.html",'r',encoding='utf-8')
src=html.read()
components.html(src)
ad = st.sidebar.slider("x")