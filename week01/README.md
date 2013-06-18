# My Notes

## What is MongoDB?
- non-relational database
- schemaless
- document-oriented (json docs)

## Mongo Relative to Relational
- Scalability & Performance vs. Depth of Functionality
    - memechached, key value stores - vs. - RDBMS
    - mongodb aims to be highly scalable and highly functional
    - requires some functional sacrifice
        - e.g. no transactions, no no joins
	- usually these are not actually necessary

## Intro to the Mongo Shell
- JSON
- Collections
- `db.collection.save({})`
- `db.collection.find()`
- `db.collection.find().pretty()`
- Subdocuments
    - Convenient for programming because it organizes data like you do in your code

## Installing MongoDB
- Google for the download
- Extract the download somewhere
- Run mongod
    - Should get an error about the nonexisting data directory
    - Go make one
    - Run `mongod` in one window, and `mongo` in another. Insert something, query something.

## Installing Bottle and Python
- Google for the Python 2.7 download
- Install setup tools, which provides `easy_install`
- Install bottle via `easy_install`
- Install pymongo
