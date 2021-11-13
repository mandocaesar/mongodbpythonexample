import pymongo
from person import Person


#create a client's connection to database
client = pymongo.MongoClient("mongodb://localhost/mydb")

#create db instance
mydb = client["mydb"]

#create collections instance
mycollection = mydb["person"]

#instantiate array of person
persons = [
    Person("Bohemian", 30).__dict__, 
    Person("Mary Jane", 21).__dict__, 
    Person("Guru", 101).__dict__
    ]


#invoke insert command and get generated id
insertedResult = mycollection.insert_many(persons)

print(insertedResult.inserted_ids)
