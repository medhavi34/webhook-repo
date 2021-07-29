import pymongo 

client = pymongo.MongoClient("mongodb+srv://admin:medhavi123@cluster0.ttqab.mongodb.net/TechStaX?retryWrites=true&w=majority")
db = client['TechStaX']
collection =db['TechStaX']

#get insert data into the database
def insert(data): 
    collection.insert_one(data)

#get all the values from MongoDB
def get(): 
    return collection.find({})
