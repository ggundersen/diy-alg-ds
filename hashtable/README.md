Hash table
==========

A hash table is a data structure that implements an associative array, mapping keys to values. A hash function efficiently generates indices from the keys added to the hash table. When a hash function produces the same index from two distinct keys, the event is called a "collision."

Hashing is a good example of a space-time tradeoff. With infinite space, we could use the key as an index in a large array. This is prohibitive since the number of possible keys is massive. With infinite time, we could search sequentially.
