from flask import Flask, render_template, request, jsonify
import pymongo
import json
import datetime
from bson import json_util

# mongodb datbase info
database = "AWS"
collection = "AWS_Conv"
# connection string
myclient = pymongo.MongoClient("mongodb+srv://mynde76:W9tWqzT3aiQa1bG0@cluster0.tuhtz5n.mongodb.net/test")
mydb = myclient[database]
col = mydb[collection]

app = Flask(__name__)

# assuming NiFi is sending data in post method
@app.route('/', methods=['POST'])
def handle_add():
    data = request.get_json() # getting data from the request
    data['added_on'] = datetime.datetime.now() # adding add_on date to the data we get
    col.insert_one(data) #sending data to mongodb
    return "Data Added"

if __name__ == '__main__':
    app.run(port=8000)
#     port the application is running on
