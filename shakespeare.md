# To be or not to be

## ~~That is the question~~ These are the questions

4.1. 1000

4.2. update_fitness is passed an array of chars called self.genes, with 18 randomly generated genes (chars) in it.
     It has a score counter initialized to equal 0. The for loop iterates through all 18 characters of self.genes,
     comparing the ascii values to those of the corresponding char in the target "to be or not to be". The target
     also has 18 characters, so each character has something to be compared against. Each time the ascii values match,
     the score counter increases by 1. At the end, fitness is determined by taking the ratio of matches to the length
     of the strings, in this case 18.

4.3. 0.05555555555555555

4.4. Edit distance reveals the minimum number of edits (substitutions, insertions, deletions) to transform one string
     another. Fitness could be determined using this function by taking the total number of characters in the target
     string as the denominator, and the minimum number of required edits as the numerator (as a float), and calculating
     that ratio.

4.5. script.py "mutates" the child strings to add some variance to the gene pool. There needs to be some random variation
     for script to even be able to trend towards the target. Mutations are the only source of change. Mutations that increase
     fitness are favored, and mutations that decrease fitness aren't, and this "favor" over a number of iterations should
     cause the overall population to be more similar to the target text.

## Debrief

a. https://www.python-course.eu/levenshtein_distance.php

b. 45 minutes
