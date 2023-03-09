# Files
### Python use file objects to interact with external files in your computer. These file objects can be any sort of file you have in your computer, wheter it be an audio file, text, emails, excel etc..., Note: You will probably need to install certain libraries or modules to interact with those various file types, but they are easily avaible and python has a built-in open function that allows us to open and play with basic file types.
<br>

## Opening a file
### Let's being by opening the file test.txt that is located in the same directory as this notebook. For now we will work with files located in the same directory as the notebook or .py script you are using. It is very easy to get an error on this step:
````
myfile = open('whoops.txt')

---------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-1-dafe28ee473f> in <module>()
----> 1 myfile = open('whoops.txt')

FileNotFoundError: [Errno 2] No such file or directory: 'whoops.txt'
--------------------------------------------------------------

# To avoid this error,make sure your .txt file is saved in the same location as your notebook, to check your notebook location, use pwd:
pwd -> 'C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\00-Python Object and Data Structure Basics'

````
* ### For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:
    * myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")

* ### For MacOS and Linux you use slashes in the opposite direction:
    * myfile = open("/Users/YouUserName/Folder/myfile.txt")
<br>

## Reading a file
`````
# Open the text.txt we made earlier
my_file = open('test.txt')

# We can now read the file
my_file.read() -> 'Hello, this is a quick test file.'

# But what happens if we try to read it again?
my_file.read() -> ''
`````
* ### This happens because you can imagine the reading "cursor" is at the end of the file after having read it. So there is nothing left to read. We can reset the "cursor" like this:
`````
# Seek to the start of file (index 0)
my_file.seek(0)

# now read the file again
my_file.read() -> 'Hello, this is a quick test file.'
`````
<br>

* ### You can read a file line by line using the readlines method. Use caution with large files, since everything will be held in memory. We will learn how to iterate over large files later in the course.
`````
# Readlines returns a list of the lines in the file
my_file.seek(0)
my_file.readlines() -> ['Hello, this is a quick test file.']
`````
### When you have finished using a file, it is always good practice to close it.
`````
my_file.close()
`````
<br>

## Writing to a file
### By default, the open() function will only allow us to read the file. We need to pass the argument 'w' to write over the file. For example:
````
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

my_file = open('test.txt','w+')
````
## Caution!!
### Opening a file with 'w' or 'w+' truncates the original, meaning that anything that was in the original file is deleted!, to adding more lines you have to append not write
`````
# Write to the file
my_file.write('This is a new line')

# Read the file
my_file.seek(0)
my_file.read()

my_file.close()  # always do this when you're done with a file
`````
<br>

## Appending to a file
### Passing the argument 'a' opens the file and puts the pointer at the end, so anything written is appended. Like 'w+', 'a+' lets us read and write to a file. If the file does not exist, one will be created.
````
my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')

my_file.seek(0)
print(my_file.read()) -> This is a new line
                        This is text being appended to test.txt
                        And another line here.
my_file.close()
````
<br>

## Iterating through a file
### Lets get a quick preview of a for loop by iterating over a text file.
`````
for line in open('test.txt'):
    print(line)

# Output:
First line
Second line
`````
* ### Don't worry about fully understanding this yet, for loops are coming up soon. But we'll break down what we did above. We said that for every line in this text file, go ahead and print that line. It's important to note a few things here:
    * ### 1 - We could have called the "line" object anything (see example below).
    * ### 2 - By not calling .read() on the file, the whole text file was not stored in memory.
    * ### 3 - Notice the indent on the second line for print. This whitespace is required in Python.
````
# Pertaining to the first point above
for asdf in open('test.txt'):
    print(asdf)

# Output:
First line
Second line
````
