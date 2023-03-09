# Strings
### Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

This idea of a sequence is an important one in Python and we will touch upon it later on in the future.
### Now we'll learn about the following topics:
* 1- Creating strings
* 2 - Printing strings
* 3 - String Indexing and slicing
* 4 - String methods
* 6 - Print formatting
<br>

## Creating a String
### To create a string in Python you need to use either single quotes or double quotes. For example:
````
# Single word
'hello'

# Entire phrase 
'This is also a string'

# We can also use double quote but if you use keep with this pattern
"String built with double quotes"

# Be careful with quotes!
' I'm using single quotes, but this will create an error'
````
<br>

## Printing a string
### To print a string you can use the built in method print to output you variable or value
`````
print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')
print('See what I mean?')
`````
<br>

## Checking string size
### You can check the string lenght using the built in function called len()
`````
len('Hello World')
`````
<br>

## String Indexing
### We know strings are a sequence, which means Python can use indexes to call parts of the sequence. Let's learn how this works.
### In Python, we use brackets [] after an object to call its index. We should also note that indexing starts at 0 for Python. Let's create a new object called s and then walk through a few examples of indexing.
````
# Assign s as a string
s = 'Hello World'
print(s) -> 'Hello World'

s[0] -> 'H'
s[1] -> 'e'
````
* ### And we can use something called slice to take only the indexes that we want:
![](https://i.stack.imgur.com/IVkET.jpg)
### Slice structure:
`````
[start:end:steps]

start: the index that you want to start

end: Where you want go to, but remember it doesnt take the exact index it goes there but takes the index before, for example:
    nome = 'joao'
    nome[0:3] -> 'joa'

steps: It works setting an interval that you want to take for the indexes if you set [0:9:2]
     - It will go from the first index with an interval of two indexes to the nine not including the 9th index.
`````
<br>

## Strings are Immutable
### It's important to note that strings have an important property known as immutability. This means that once a string is created, the elements within it can not be changed or replaced. For example:
`````
# Let's try to change the first letter to 'x'
s[0] = 'x'

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-26-976942677f11> in <module>()
      1 # Let's try to change the first letter to 'x'
----> 2 s[0] = 'x'

TypeError: 'str' object does not support item assignment
---------------------------------------------------------------

# but we can concatenate it
new_string = s + 'Good morning'
print(new_string)

# And We can use the multiplication symbol to create repetition!

letter = 'z'
letter*10 -> 'zzzzzzzzzz'
`````
<br>

## Basic String built in methods
### Objects in Python usually have built-in methods. These methods are functions inside the object (we will learn about these in much more depth later) that can perform actions or commands on the object itself.
*  We call methods with a period and then the method name. Methods are in the form:
    * ### object.method(parameters)
````
s = 'Hello World'

# Upper case string
s.uper() -> 'HELLO WORLD'

# Lower case string
s.lower() -> 'hello world'

# Split by a specific element or blank space by default(doesn't include the element that was split on)
s.split('W') -> ['Hello', 'orld']
````
<br>

## Printing format
### We can use the .format() method to add formatted objects to printed string statements.
`````
'Insert another string with curly brackets: {}'.format('The inserted string')
`````
* ### And in python 3 appeard a new option of string concatenation that is a sugar syntax .format
````
name='joao'
print(f'Hello World {name}')
````

