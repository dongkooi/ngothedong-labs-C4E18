#Database
#Collection
#Document
#pymongo
from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin123@ds053469.mlab.com:53469/c4e18-lab"
# 1. Connect to database
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Create collection
games = db['games']
film = db['Adult']
# 4. Create document
# new_film = {
#     "title": "50 shades",
#     "description": "Adult film"
# }
# 5. Insert document into collection
# film.insert_one(new_film)

all_game = games.find()

for game in all_game:
    print(game)