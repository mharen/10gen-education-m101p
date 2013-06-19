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

## JSON Revisited
- Arrays
- Dictionaries
- Subdocuments
- Spec

## Introduction to Class Project
- A simple blog engine
- Modeling the blog in a relational database
    - posts, authors, comments, tags, etc. are spread out across different tables
- Modeling the blog in MongoDB
    - posts, authors, comments, tags, etc. are all included in a single document 
	  (with arrays and subdocuments)
	- can use natural data as the unique ID in a collection, e.g. author. 
	  i.e. use `{ author: 'mharen' }` in the posts collection, and use 'mharen' as the `_id` 
	  in the `authors` collection
	
## Introduction to Schema Design
- To Embed or Not to Embed. That is the question
- Let the way want to access your data guide you

## Introduction to Python
- lists
- dicts
- loops
- conditionals
- function calls
- exception handling

## Bottle Framework
- url handlers
- views/templates
- form content
- cookies
- debugging: 
    - `bottle.debug(True)`
	- `bottle.run(host="localhost", port="8080")
- redirects

## The Pymongo Driver

## HW1






