#!/usr/bin/env python
# coding: utf-8

# In[3]:

import streamlit as st
st.markdown('<style>body{background-color: DarkSeaGreen;}</style>',unsafe_allow_html=True)
st.title("SIMLARITY SEARCH IMPLEMENTATION")
html_temp = """<body style="background-color:grey>
</body>
"""
st.markdown(html_temp,unsafe_allow_html=True)
html_temp = """
<div style="background-color:Crimson;padding:10px">
<h2 style="color:black;text-align:center;">Streamlit App for Similar Products </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
#st.text("Upload an Image to find similar Products")
import glob
import keras
from PIL import Image, ImageOps
import numpy as np
import pandas as pd

def get_data():
    return pd.read_csv('streamlit.csv',header=None)
n=1
df = get_data()
images = df[0].unique()
st.subheader("Choose an image from the below list : ")
pic = st.selectbox('Images : ', images)
st.subheader("Image Selcted")
st.image(pic,width=None)
st.subheader("Similar Products")
for index, row in df.iterrows():
    if row[0]==pic:
        while n < 21:
            st.image(row[n], use_column_width=None, caption=row[n])
            n+=1
