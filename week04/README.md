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
