import pymongo
from person import Person


#create a client's connection to database
client = pymongo.MongoClient("mongodb://localhost/mydb")

#create db instance
mydb = client["mydb"]

#create collections instance
mycollection = mydb["person"]

#instantiate person class to an object then insert it to collection
person = Person("John doe", 30)

#invoke insert command and get generated id
insertedId = mycollection.insert_one(person.__dict__)

print(insertedId)
