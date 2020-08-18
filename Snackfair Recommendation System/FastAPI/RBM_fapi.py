import uvicorn
from fastapi import FastAPI,Query
import joblib
import csv
import pandas as pd

# init app
app = FastAPI(title="Restricted Boltzmann Machine (RBM)",
              description='''A Restricted Boltzmann Machine (RBM) is a generative neural network model typically used to perform unsupervised learning.''',
              version="0.1.0",)

# Routes
@app.get('/')
async def index():
    return {"text":"Hello"}

@app.get('/items/{user_id}')
async def get_users(user_id:int):
    return {"user_id":user_id}

@app.get('/items/{item_id}')
async def get_items(item_id:int):
    return {"item_id":product_id}

# ML Aspect
@app.get('/predict/')
async def predict(user_id:int = 1, item_id:int = 70128):
    
    dataframe = pd.read_csv("RBM.csv")
    prediction = dataframe.loc[(dataframe['userID'] == user_id) & (dataframe['itemID'] == item_id), ['prediction']]

    return {"prediction":prediction}

if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
