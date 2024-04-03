# Notes
## a trie can check if a string is a valid prefix in O(K) time, where K is the length of the string. 
This is actually the same runtime as a hash table will take. Although we often rfere to hash table looksups as being O(1) time, this isn't entirely true. A hash table must read through all the characters in the input, which takes O(K) time in the case of a word lookup.

# ways to represent a graph: 
## adjacency list
Every vertex (or node) stores a list of adjacent vertices.
In an undirected graph, an edge like (a, b) would be stored twice: once in a's adjacent vertices and once in b's adjacent vertices. 

