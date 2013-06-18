import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection.test
names = db.names
item = names.find_one()

print item['name']


# to run this file:
# 1. start the local mongod server
# 2. Insert some data into the names collection: `db.names.save({ name: 'michael' })`
# 3. Run this file with `python pymongo-getting-started.py`
