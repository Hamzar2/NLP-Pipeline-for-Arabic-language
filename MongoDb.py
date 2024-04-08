from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://hamzadr2:azer1234@cluster0.feu8uxm.mongodb.net/")

db = client['arabic_scrapy']
collection = db['arabic']
with open("myproject\output.json",'r', encoding='utf-8') as data:
    doc = json.load(data)

if isinstance(doc , list):
    for obj in doc:
        print(obj)
        collection.insert_many(doc)

