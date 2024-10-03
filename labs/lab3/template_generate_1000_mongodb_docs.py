# pip install Flask-PyMongo
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://i40:dbms2@cluster0.lixbqmp.mongodb.net/lab3"
mongo = PyMongo(app)
all = mongo.db.test2.find()

mongo.db.test2.delete_many({})

for i in range(1000):
    o = {"uuid":i, "source":"mongodb", "creationTimestamp":12345, "updatedTimestamp":12345, "A":"A", "B":"B", "C":"C"}
    print(o)
    mongo.db.test2.insert_one(o)
