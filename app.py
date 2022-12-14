from flask import Flask,render_template,session
from pymongo import MongoClient
from flask_pymongo import pymongo
from bson import json_util
import json

import json



app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://gowthamthota:Data2022@cluster0.plhhagn.mongodb.net/?retryWrites=true&w=majority")
db  = client["nursery"]
collection = db["seeds1"]

# db = client.nursery
# cursor = db.seeds1.find({'baseAsset':'btc'})

#client = pymongo.MongoClient("mongodb+srv://gowthamthota:Data2022@cluster0.plhhagn.mongodb.net/?retryWrites=true&w=majority")

@app.route('/')
def getdata():
    #return render_template('index.html')
    # return "hey"
    all_seeds = list(collection.find({"symbol":"btcinr"}))
    return  json.dumps(all_seeds, default=json_util.default)



