from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import url_for
from flask_pymongo import PyMongo
import base64
import boto3
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'first'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Assignment_2'
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('team8')
mongo = PyMongo(app)
@app.route('/category/<cid>', methods=['GET'])
def get_all_stars(cid):
  output =[]
  s=""
  pre ="products/"+cid
  for object_summary in my_bucket.objects.filter(Prefix=pre):
     print(object_summary.key)
     output.append(object_summary.key)
  for  out in output:
      fileO = "https://team8.s3.amazonaws.com/"+out
      s = s+ f"<img src='{fileO}' />"
  return s 
if __name__ == '__main__':
    app.run(debug=True)