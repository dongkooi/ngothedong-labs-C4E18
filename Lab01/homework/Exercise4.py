import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# 1. Connect to database
client = MongoClient(mongo_uri)
# 2. Get database
db = client.get_default_database()
# 3. Create collection
customers = db['customers']

labels = ["events","wom", "ads"]
values = [customers.find({"ref":"events"}).count(), customers.find({"ref":"wom"}).count(), customers.find({"ref":"ads"}).count()]
colors = ['red', 'green', 'gold']
explode = [0, 0, 0]
pyplot.pie(values, 
            labels = labels, 
            colors = colors,
            explode = explode)
pyplot.axis("equal")
pyplot.show()

# Hàm count() cách lấy từ db search từ https://docs.mongodb.com/manual/reference/method/cursor.count/