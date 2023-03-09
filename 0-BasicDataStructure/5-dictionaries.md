# Dictionaries
### We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.
### Now we'll learn about the following topics:
* 1- Constructing a Dictionary
* 2 - Accessing objects from a dictionary
* 3 - Nesting Dictionaries
* 4 - Basic Dictionary Methods
<br>

## So what are mappings ? 
###  Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.
<br>

## Constructing a Dictionary:
``````
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

# Call values by their key
my_dict['key2'] -> 'value2'
``````
* ### Its important to note that dictionaries are very flexible in the data types they can hold. For example:
`````

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Let's call items from the dictionary
my_dict['key3'] -> ['item0', 'item1', 'item2']

# Can call an index on that value
my_dict['key3'][0] -> 'item0'

# Can then even call methods on that value
my_dict['key3'][0].upper() -> 'ITEM0'
------------------------------------------------------
# We can affect the values of a key as well. For instance:
my_dict['key1']

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123

#Check
my_dict['key1'] -> 0

# Can be like this too:
my_dict['key1'] -= 123
`````
* ### We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:
````
# Create a new dictionary
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

d -> {'animal': 'Dog', 'answer': 42}
````
<br>

## Nesting Dicts
### Hopefully you're starting to see how powerful Python is with its flexibility of nesting objects and calling methods on them. Let's see a dictionary nested inside a dictionary:
`````
# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# Grabbing  the value
d['key1']['nestkey']['subnestkey'] -> 'value'
`````
<br>

## Few Dictionary methods
### There are a few methods we can call on a dictionary. Let's get a quick introduction to a few of them:
* ### Keys()
````
# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}
# Method to return a list of all keys 
d.keys()
````
* ### Values()
````
d.values() -> dict_values([1, 2, 3])
````
* ### Items()
````
d.items() -> dict_items([('key1', 1), ('key2', 2), ('key3', 3)])
````

