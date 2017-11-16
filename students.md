# Comparing Students

## Questions

1.1. It represents the comparsion function, that decides if one argument should come before or after the other, then returns a positive integer (1) or a negative integer (-1) according to which
     way you want to sort. If the arguments are equal, it returns a value of 0.

1.2. Since we are using qsort, the comparison function must have (const void *x) types as parameters. We know that the data type being pointed to is an int, and we want our new pointers to acknowledge
     that so our int variables arg1 and arg2 can recieve the int values being pointed to. We use const because we only want to read the values being used for the comparison, not to change them. Also,
     you can't point to a variable of type "const type" without the pointer also being of type "const type"-- the code won't compile.


1.3. See `students.c`.

1.4. See `students.py`.

1.5. See `students.js`.

## Debrief

a. https://www.tutorialspoint.com/c_standard_library/c_function_strcmp.htm
   https://stackoverflow.com/questions/28396382/casting-a-const-void-to-a-const-char-in-c
   https://wiki.python.org/moin/HowTo/Sorting#Key_Functions
   console.log("hello, world");

b. 2 hours
