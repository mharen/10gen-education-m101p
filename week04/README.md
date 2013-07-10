# My Notes - Week 4 - Performance

## Indexes
- Creating indexes
- Discovering indexes
- Multikey indexes (indexes including an array value)
    - Can index values in arrays, but not multiple arrays in the same index
- Sparse indexes
- Unique indexes
- Removing dupes
- Background vs. foreground creation
- Using `.explain()`
- How Mongo chooses an index to use
- Cardinality
    - Regular indexes: index points = # documents
    - Sparse indexes: index points <= # documents
    - Multikey: index points > # documents
        - Warning: this implies that updating an array with 100 elements requires 100 index point updates, too
- Selectivity
    - Try to be as selective as possible
- Hinting an index, e.g. `.hint({ a: 1, b: 1 })` or, to not use an index: `.hint({ $natural: 1 })`
    - Hinting in pymongo, e.g. `.find(query).hint([('a', pymongo.ASCENDING)])`
- Geospatial indexes
    - `.ensureIndex({ location: '2d', foo: 1 })` 
    - `.find({ location: { $near: [x, y] } })`
        - returns docs in increasing distance (often used with `.limit(n)` to retrieve "_n_ closest docs"
- Geospatial _spherical_ model
    - still use same '2d' index
    - locations are specified the same, `[longitude, latitude]`
    - query uses `runCommand` and `geoNear`, e.g.:
        - `db.runCommand({ geoNear: 'stores', near: [50,50], spherical: true, maxDistance: 1 })`
        - max distance is in radians (arc distance on surface of earth, e.g. [0, 2pi])
- Logging slow queries
    - Queries longer than 100ms are automatically logged (no profiler required)
- Profiler
    - three modes: 0: off, 1: slow queries, 2: everything
    - enable from command line, `--profile 1 --slowms 2`
    - or from shell, `db.getProfilingStatus()`, `db.setProfilingLevel(1 /*mode*/, 2 /*ms*/)`
    - results in `db.system.profile`
- `mongotop`, named for Unix's `top`, shows where the db is spending its time
- `mongostat`, named for Unix's `iostat`, for detailed db status including index misses, etc.
- Sharding overview
    - Split collections up across many instances of mongod, or replica sets
    - Splits are made by shard key
    


