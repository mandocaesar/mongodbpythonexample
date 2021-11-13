import pymongo
from person import Person


#create a client's connection to database
client = pymongo.MongoClient("mongodb://localhost/mydb")

#create db instance
mydb = client["mydb"]

#create collections instance
mycollection = mydb["person"]

#query data to be updated
myquery = {"name":"Mary Jane"}
newvalues = {"$set":{"age":900}}

#invoke delete command
mycollection.update_one(myquery,newvalues)

#iterate on collection then print it to see if the data has been updated
for x in mycollection.find():
    print(x)