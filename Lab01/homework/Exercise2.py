
from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# 1. Connect to database
client = MongoClient(mongo_uri)
# 2. Get database
db = client.get_default_database()
# 3. Create collection
posts = db['posts']
customers = db['customers']
# 4. Create document
new_post = {
    'title':'DSK',
    'author':'NTD',
    'content':'Người như cây củi, 1 mét 73'
    }
# 5. Insert document into collection
posts.insert_one(new_post)

