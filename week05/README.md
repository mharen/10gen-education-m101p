# My Notes - Week 5 - Aggregation

## Indexes
- Introduction to aggregation
- Pipeline stages
    - `$group`
    - `$project`
    - `$match`
    - `$sort`
    - `$skip`
    - `$limit`
    - `$unwind`
- Compound grouping
- Lots of aggregation operators
- Chaining multiple stages together
- Mapping between SQL and aggregation
- SQL examples implemented as aggregations
- Limitations
    - 16 mb output
    - 10% server memory
    - significant implications for sharded environments
- Alternatives
    - mapreduce
    - hadoop