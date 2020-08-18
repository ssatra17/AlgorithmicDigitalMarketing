import uvicorn
from fastapi import FastAPI,Query
import joblib

# Models
rlrmc = open("RLRMC.sav","rb")
rlrmc_model = joblib.load(rlrmc)

# init app
app = FastAPI(title="Riemannian Low-rank Matrix Completion algorithm",
              description='''Riemannian Low-rank Matrix Completion (RLRMC) is a matrix factorization based (vanilla) matrix completion algorithm that solves the optimization problem using Riemannian conjugate gradients algorithm.''',
              version="0.1.0",)

# Routes
@app.get('/')
async def index():
	return {"text":"Hello"}

@app.get('/user/{user_id}')
async def get_users(user_id:int):
	return {"user_id":user_id}

@app.get('/product/{item_id}')
async def get_item(item_id:int):
	return {"item_id":item_id}

# ML Aspect
@app.get('/predict/')
async def predict(user_id:int = 1, item_id:int = 3342):
	user_list = []
	item_list = []
	user_list.append(user_id)
	item_list.append(item_id)
	prediction = rlrmc_model.predict(user_list, item_list)
	if prediction[0] > 0:
		result = prediction[0]
	else:
		result = "Not Found"

	return {"prediction":result}

if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
