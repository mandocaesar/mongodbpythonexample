import pymongo
from person import Person


#create a client's connection to database
client = pymongo.MongoClient("mongodb://localhost/mydb")

#create db instance
mydb = client["mydb"]

#create collections instance
mycollection = mydb["person"]

#specified which data to be deleted
myquery = {"name":"Bohemian"}

#invoke delete command
mycollection.delete_one(myquery)

#iterate on collection then print it to see if the data has been deleted
for x in mycollection.find():
    print(x)