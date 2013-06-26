# My Notes - Week 2

## CRUD and the Mongo Shell
- It's mostly javascript
- BSON
    - A superset of JSON
    - Types
- `insert`
- `find`, `findOne`
- query operators
- queries with dot notation
    - `db.users.find({ "email.work": "foo" })`
    - `              that----^
- cursors
    - `next()`, `hasNext()`
    - `while(cur.hasNext()) printjson(cur.next())`
    - you can modify the cursor up to the point that you start retrieving documents, e.g. `.limit(5)`, `.sort({name:-1})`, `.limit(5)`, `.skip(5)`
        - these methods affect the query that is made to the db so you can't use them after the query has been sent
        - these are processed on the server, not the client
    - prevent shell from enumerating cursor at declaration by adding `null`: `var c = db.users.find(); null;`
- `update`    
    - replace document
    - `$set` fields
    - `$unset` fields
    - `$inc{ field: increment_amount }`
    - arrays: 
        - `$set`: update value in an array: `$set: { "a.2": 5 }` sets the third value in the array `a` to 5
        - `$pop`: remove from end of array (1) or beginning of array (-1): `$pop: { a: 1 }`
        - `$push`: append to end of array
        - `$pushAll: { a: [1,2,3] }`: add all elements to array
        - `$pull: { a: 5 }`: remove any item by value
        - `$pullAll: { a: [1,2,3] }`: remove all items by value
        - `$addToSet: { a : 5 }`: pushes item if it doesn't exist
- upserts with `.update({},{},{ upsert: true })` 
- multi-update with `.update({},{}.{ multi: true })` (without `{multi:true}` an `update` affects only a single document)
    - not atomic among documents
- removing data with `.remove({})` (this is a multidoc operation--passing in an empty query will remove *all documents*)
    - not atomic among documents
- `.drop()` removes all documents, indexes, etc. from a collection
    - vastly faster than `.remove()`, but drops indexes, etc., too (`.remove` does not)

## Error Handling
- the shell automatically checks for errors after every command
- `db.runCommand({ getLastError: 1 })`
    - gives more details about the last command
        - tells you if an upsert was an update or insert
        - tells you how many docs were updated in a multi-update
        - tells you how many docs were removed with a `remove()` operation
        - error details if an error occurred


