import pymongo
import json
import glob
import os
import pprint

cwd = os.getcwd()

from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
#need to find better way to find mongo client ...
client = MongoClient('mongo', 27017) 
db = client.shellfish_db
collection = db.employee

os.chdir(cwd+'/expertise_finder_profile')
jsonFiles = glob.glob("*.json")
for file in jsonFiles:
	f = open(file, 'r')
	json_data = f.read()
	data = json.loads(json_data)[0]
	postid = collection.insert_one(data).inserted_id
	print ('inserted with id: ', postid)
	
	f.close()