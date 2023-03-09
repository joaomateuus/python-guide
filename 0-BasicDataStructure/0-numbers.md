# Numbers 
### In this lecture, we will learn about numbers and how to use them.
### We'll learn about the following topics:
* 1- Types of numbers in python.
* 2 - Basic Arithmetic.
* 3 - Differences between classic division and floor division.
* 4 - Object Assignment in python.
<br>
<br>

## Types of numbers:
### Python has various "types" of numbers (numeric literals). We'll mainly focus on integers and floating point numbers.
### Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
### Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.

<table>
    <tr>
        <th>Examples</th>
        <th>Number / Type</th>
    </tr>
    <tr>
    <td>1,2,-5,1000</td>
     <td>Integers</td>
    </tr>
    <tr>
        <td>1.2, -0.5, 2e2, 3E2</td> 
        <td>Floating-point numbers</td>
    </tr>
</table>
<br>

## Basic Arithmetic
`````
# Addition
2 + 1 -> 3

# Subtraction
2 - 1 -> 1

# Multiplication
2 * 2 -> 4

# Division
3 / 2 -> 1.5

# Remainder
7 % 4 -> 3

# Floor Division
7 / / 4 -> 1
`````

* Why floor divison its not equals to 1.75 ?
    * The reason we get this result is because we are using "floor" division. The // operator (two forward slashes) truncates the decimal without rounding, and returns an integer result.
<br>

## Arithmetic continued
````
# Powers
2**3 -> 8

# Can also do roots this way
4**0.5 -> 2.0

# Order of Operations followed in Python
2 + 10 * 10 + 3 -> 105

# Can use parentheses to specify orders
(2+10) * (10+3) -> 156
````
<br>

## Creating variables
### We use a single equals sign to assign labels to variables. Let's see a few examples of how we can do this.
````
a = 5
a + a -> 10

# Reassignment
# Reassignment
a = 10 -> 10
````
* ### Yes! Python allows you to write over assigned variable names. We can also use the variables themselves when doing the reassignment. Here is an example of what I mean:
````
a -> 10
a = a + 1
a -> 20
````
<br>

### And there are a few rules that we have to keep in mind when we are creating python variables:
````
1. Names can not start with a number.
2. There can be no spaces in the name, use _ instead.
3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
4. It's considered best practice (PEP8) that names are lowercase.
5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), 
   or 'I' (uppercase letter eye) as single character variable names.
6. Avoid using words that have special meaning in Python like "list" and "str"
````

### Using variable names can be a very useful way to keep track of different variables in Python. For example:
````
# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

my_taxes -> 10.0
````