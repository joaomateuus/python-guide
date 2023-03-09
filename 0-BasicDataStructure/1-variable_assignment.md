# Variable Assignment
### In the last chapter we saw a little bit about it and we'll get more deep into now.
<br>

## Variable Name Rules
* Names can not start with a number
* Names can not contain spaces, use _ intead
* Names can not contain any of these symbols: :'",<>/?|\!@#%^&*~-+
* It's considered best practice (PEP8) that names are lowercase with underscores
* Avoid using Python built-in keywords like list and str
* Avoid using the single characters l (lowercase letter el), O (uppercase letter oh) and I (uppercase letter eye) as they can be confused with 1 and 0
<br>

## Dynamic Typing
### Python uses dynamic typing, meaning you can reassign variables to different data types. This makes Python very flexible in assigning data types; it differs from other languages that are statically typed, even though we can strictly type our variables too but its optional.
`````
my_dogs = 2
my_dogs -> 2

my_dogs = ['Sammy', 'Frankie']
my_dogs -> ['Sammy', 'Frankie']
`````
* ## Pros and Cons of Dynamic Typing
    * ### Pros:
        * Very easy to work with
        * Faster development time
     * ### Cons:
        * May result in unexpected bugs
        * You need to be aware of type()