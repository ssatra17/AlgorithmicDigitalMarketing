import streamlit as st
#from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from PIL import Image
import io
import joblib
from RLRMC_fapi import predict
import pandas as pd
st.markdown('<style>body{background-color: cornsilk;}</style>',unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; color: black;'>Snack Recommendations!!</h1>", unsafe_allow_html=True)
#st.title('Snack Recommendations!!')
#st.markdown(html_temp,unsafe_allow_html=True)
html_temp = """
<div style="background-color:Crimson;padding:10px">
<h1 style="color:black;text-align:center;">Snack Recommendation!! </h1>
</div> """
st.markdown(html_temp,unsafe_allow_html=True)  
st.write('') 
image = Image.open('snacks.jpg')

st.image(image, caption='Snack Recommendation',use_column_width=True)

title = st.number_input('User ID',min_value = 0,max_value=100000,value = 0,step =1)

pro = st.number_input('Pro ID',min_value = 0,max_value=1000000,value = 0,step =1)

algos = ['RLRMC','RBM']
choices = st.sidebar.selectbox("Select Algorithms",algos)

def get_data(user_id,pro_id):
    server_url = url + endpoint + str(user_id) + ',' + str(pro_id)
    r= requests.get(server_url)
    return r.json()

if choices == 'RLRMC':
    url = 'http://127.0.0.1:8001/'
    endpoint = 'predict/'


    if st.button('Get Prediction value'):
        #st.write('hello')
        segments = get_data(title,pro)
        st.write(segments)

    if st.button('Get Recommendations'):
        data = pd.read_csv('RLRMC.csv')  
        df1 =  data['userID']==title
        df2 =data[df1]
        if df2.empty:
            st.write('we have no information on this user!')
        else:
            st.write(df2.head())

if choices == 'RBM':
    url = 'http://127.0.0.1:8000/'
    endpoint = 'predict/'


    if st.button('Get Prediction value'):
        segments = get_data(title,pro)
        st.write(segments)

    if st.button('Get Recommendations'):
        data = pd.read_csv('RBM.csv')  
        df1 =  data['userID']==title
        df2 =data[df1]
        if df2.empty:
            st.write('we have no information on this user!')
            
        else:
            
            st.write(df2.head())