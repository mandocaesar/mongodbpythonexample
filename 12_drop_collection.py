import pymongo
from pymongo import collection
from person import Person


#create a client's connection to database
client = pymongo.MongoClient("mongodb://localhost/mydb")

#create db instance
mydb = client["mydb"]

#create collections instance
mycollection = mydb["person"]

#drop collection
result = mycollection.drop()

#print result , returns empty if the collection does not exist.
for x in  mydb.list_collection_names():
    print(x)