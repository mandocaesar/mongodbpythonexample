import pymongo
from person import Person


#create a client's connection to database
client = pymongo.MongoClient("mongodb://localhost/mydb")

#create db instance
mydb = client["mydb"]

#create collections instance
mycollection = mydb["person"]

#define a query
myquery = {"name":"John doe"}

#iterate on collection then print it
for x in mycollection.find(myquery):
    print(x)
