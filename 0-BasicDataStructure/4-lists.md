# Lists
### Earlier when discussing strings we introduced the concept of a sequence in Python. Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed!
### Now we'll learn about the following topics:
* 1- Creating lists
* 2 - Indexing and Slicing Lists
* 3 - Basic List Methods
* 4 - Nesting Lists
* 6 - Introduction to List Comprehensions
<br>

## Structure:
### Lists are constructed with brackets [] and commas separating every element in the list.
````
# Assign a list to an variable named my_list
my_list = [1,2,3]

# We just created a list of integers, but lists can actually hold different object types. 
my_list = ['A string',23,100.232,'o']

# Just like strings, the len() function will tell you how many items are in the sequence of the list.
len(my_list)
````
<br>

## Index and Slicing
### Indexing and slicing work just like in strings. Let's make a new list to remind ourselves of how this works:
````
my_list = ['one','two','three',4,5]
my_list[0] -> 'one'

# Grab index 1 and everything past it
my_list[1:] -> ['two', 'three', 4, 5]

## Grab everything UP TO index 3
my_list[:3] -> ['one', 'two', 'three']
````
* ### Remember that a list has a size and if you try to acess an index that doesnt exist it will raise an error:
`````
list1[100]
---------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-22-af6d2015fa1f> in <module>()
----> 1 list1[100]

IndexError: list index out of range
--------------------------------------------------------------

Instead you can always acess the last element of the list using -1:
my_list = ['one', 'two', 'three']
my_list[-1] -> 'three'
my_list[-2] -> 'two'
`````

* ### We can also concatenate like strings but it doesnt change the original list:
````
my_list + ['new item'] -> ['one', 'two', 'three', 4, 5, 'new item']

new_list = my_list + ['new item']
my_list -> ['one','two','three',4,5]
new_list -> ['one', 'two', 'three', 4, 5, 'new item']
````
* ### We can also use * for a duplication method to similar to strings, and its not permanently too since you dont assign it to a varible
`````
my_list * 2
# output: 
['one',
 'two',
 'three',
 4,
 5,
 'add new item permanently',
 'one',
 'two',
 'three',
 4,
 5,
 'add new item permanently']
`````
<br>

## Basic List Methods:
### If you are familiar with another programming language, you might start to draw parallels between arrays in another language and lists in Python. Lists in Python however, tend to be more flexible than arrays in other languages for a two good reasons: they have no fixed size (meaning we don't have to specify how big a list will be), and they have no fixed type constraint (like we've seen above).
* ## Append()
    ### Use the append method to permanently add an item to the end of a list:
    `````
    list1.append('append me!')
    list1 -> [1, 2, 3, 'append me!']
    `````
* ## Pop()
    ### Use pop to "pop off" an item from the list. By default pop takes off the last index, but you can also specify which index to pop off. Let's see an example:
    `````
    list1.pop(0) -> 1
    list1 -> [2, 3, 'append me!']

    # Here took the last one
    popped_item = list1.pop()
    popped_item -> 'append me!'

    list1 -> [2, 3]
    `````
* ## Reverse()
    ### Use reverse to reverse order (this is permanent!)
    ````
    new_list.reverse()
    new_list -> ['c', 'b', 'x', 'e', 'a']
    ````
* ## Sort()
    ### Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
    ````
    new_list.sort()
    new_list -> ['a', 'b', 'c', 'e', 'x']
    ````
<br>

## Nesting Lists
### A great feature of of Python data structures is that they support nesting. This means we can have data structures within data structures. For example: A list inside a list.
````
# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
matrix -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Grab first item in matrix object
matrix[0] -> [1, 2, 3]

# Grab first item of the first item in the matrix object
matrix[0][0] -> 1
````
<br>

## List Comprehensions
### Python has an advanced feature called list comprehensions. They allow for quick construction of lists. To fully understand list comprehensions we need to understand for loops. So don't worry if you don't completely understand this section, and feel free to just skip it since we will return to this topic later.
`````
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]

first_col -> [1, 4, 7]
`````
* ### We used a list comprehension here to grab the first element of every row in the matrix object. We will cover this in much more detail later on!