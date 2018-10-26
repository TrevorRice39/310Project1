-----------------------------------------------------------------
Radix Sort and PostFix evaluation using ArrayStack and ArrayQueue
-----------------------------------------------------------------
This project is my implementation of Radix Sort and evaluation
of Postfix notated expressions in Python 3 using custom stack
and queue data structures.

------------
Installation
------------
To run both RadixSort.py and PostFix.py you must have installed
an IDE of your choice, Python 3, and both the Array_Queue.py
and Array_Stack.py files which are included with this package.
You must decompress/extract these files into the same directory
in order for the RadixSort.py and PostFix.py to import the 
necessary files. These files are purely source code and are only 
meant to be implemented for testing or in other programs.

-------
Example
-------
In RadixSort.py there is a function named radix_sort( ) which takes
a list as an input and sorts it. To use this function you must call
it. i.e. radix_sort(yourList), which will result in yourList being
sorted in ascending order.
Example:
a = [3, 5, 1, 2, 4]
radix_sort(a)
# a = [1, 2, 3, 4, 5]

In Postfix.py there is a function named evaluate_postfix( ) which
takes a string as an argument, assuming the string is in proper
postfix notation, and outputs its value. This function returns a 
value so you can either print it or store it in a variable. i.e.
x = evaluate_postfix(yourExpression)
print(evaluate_postfix(yourExpression))

Example:
x = evaluate_postfix('12+34+*')
print(x) # prints 21


------
Author
------
Trevor Rice
trevor_rice39@mymail.eku.edu


