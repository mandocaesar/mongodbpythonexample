import pymongo

#create a client's connection to database
client = pymongo.MongoClient("mongodb://localhost/mydb")

#print database connection
databases = client.get_database()
print(databases)