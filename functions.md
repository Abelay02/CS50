# #functions

## Questions

1. TODO
if the same letter occurs multiple times in the string, they will be mapped to the same output, and many collisions will potentially occur.

2. TODO
This hash function will not have any collisions, because each unique input has a unique ASCII representation, and thus a unique output.
There will be no collisions, the hash function is perfect.

However, outputting values like 4276803 for inputs as simple as ABC, this hash function puts a huge burden on the computer's memory,
and will cause the program to run slowly as the outputs become absurdly large.


3. TODO
It's much more efficient to compare a string to a string than it is to compare a jpeg to a jpeg. This difference, across 50 images,
across hundreds of psets surely saves a significant amount of computing power and time.

If the hash function is perfect, it is an equally effective method of checking for correctness. The hash function (presumably) uses
all of the jpeg data, and the hash is solely determined by the data being hashed. The correct hash value will not be achieved by any other
jpeg, regardless of how slight the difference might be. The hash is equally unique to the jpeg, and thus equally suitable to be used
for checks.

4. TODO
these are worst case scenarios. The upper bound for lookup in a trie is O(m), with m being the length of the search string. For most english
words m is going to be a small number, and by convention we can call it O(1) (which it essentially is). For a hash table, the upper bound on
word lookup runtime is O(n) if all the different keys map to the same position on the hash table.

## Debrief

1. TODO
http://www.sparknotes.com/cs/searching/hashtables/section2.rhtml
https://en.wikipedia.org/wiki/Hash_function

2. TODO
1 hour