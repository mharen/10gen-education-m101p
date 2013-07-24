# My Notes - Week 6 - Application Engineering

## Durability of writes
- Write concern and journaling
    - `j` only affects the journal on the primary, not secondaries
    - `w=majority` is a best practice to reduce the possibility of data rollback
    - nodes will try to elect the most synced node in an election
- Network errors
    - It's possible to use `j=1,w=1`, and `try` blocks in your code, and still not receive acknowledgement that a write completed successfully because of a network error

## Availability/Fault tolerance
- Replication
- Elections
- Write consistency
- Creating and working with replica sets
- Failover and rollback
- Connecting to a replica set
- Failover details
- Surviving failover
- Read preference
    - `primary`, `secondary`, `primaryPreferred`, `secondaryPreferred`, `nearest`, _`tag`_
- Implications of replication
    - Seed lists
    - Write concern
    - Read preferences
    - Errors can happen
    
## Horizontal scaling
- Sharding
- Creating a sharded environment
- Implications
    - Every doc includes a shard key
    - Every query should use a shard key to avoid "scatter gather"
    - Unique keys must begin with the shard key so it can enforce the shard key
- Sharding + Replication
    - Sharding almost *always* uses replica sets
    - Normally run multiple `mongos` instances, and you often run them directly on the application server (they're light)
- Choosing a shard key
    - Sufficient cardinality/variety
    - Avoid montonically increasing keys (like BSON IDs), which lead to hotspots
    - Consider how the data could be naturally parallelized when choosing a key
    