from pymongo import MongoClient
import os 
# Connect to the database
import os

client = MongoClient(os.getenv("MONGOLAB"))

db = client.PyMongoLab

posts = db.posts

post = {'author':'Diego','text':'Hello world'}

id_pymongolab= posts.insert(post)

print ('Create the id: %s' % post)

client.close()