import pymongo
from person import Person


#create a client's connection to database
client = pymongo.MongoClient("mongodb://localhost/mydb")

#create db instance
mydb = client["mydb"]

#create collections instance
mycollection = mydb["person"]

#specified which data to be deleted
myquery = {"age":30}

#invoke delete command
mycollection.delete_many(myquery)

# to delete all Data in collection invoke following line
# mycollection.delete_many({})

#iterate on collection then print it to see if the data has been deleted
for x in mycollection.find():
    print(x)