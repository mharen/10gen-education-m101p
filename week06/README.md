# My Notes - Week 6 - Application Engineering

## Durability of writes
- Write concern and journaling
- Network errors
    - It's possible to use `j=1,w=1`, and `try` blocks in your code, and still not receive acknowledgement that a write completed successfully because of a network error

## Availability/Fault tolerance
- Replication
- Elections
- Write consistency
- Creating and working with replica sets
- Failover and rollback

## Horizontal scaling