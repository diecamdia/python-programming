from pymongo import MongoClient
import os 

client = MongoClient(os.getenv("MONGOLAB"))

db = client.PyMongoLab

posts = db.posts
print ('Obteniendo información...')
results_posts = db.posts.find()

for post in results_posts:
	print (post)

client.close()