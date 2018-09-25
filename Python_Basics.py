# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:46:14 2018
@author: Aveedibya Dey
"""

"""PYTHON DATATYPES:
    Source: https://www.programiz.com/python-programming/variables-datatypes
    Types: int, float, complex
    Use type() function to check the type
"""
a = 5
type(a)
print(a, "is of type", type(a))

a = 2.0
type(a)
print(a, "is of type", type(a))

a = 1+2j
type(a)
print(a, "is complex number?", isinstance(1+2j,complex))

#-------------------------------------------------------------
"""Sets: Python Datatype"""

a = {1,2,3,4,5,6} 
#Note: We also use curly brackets for dictionaries, but define differently
#Set will always have unique values only 
#and they are always ordered in asc order

b = {1,2,2,3,4,3,4,5,6}
b==a
#Should be True

b = {3,2,4,1,2,5,6}
b==a
#Should be False? or True?

#Indexing has no meaning in Sets
#Perform set like operations  - Refer 8.7.1 in Documentation
#Source: https://docs.python.org/2/library/sets.html

#-------------------------------------------------------------
"""PYTHON FUNCTIONS"""

"""
Basics of Function:
> Keyword def marks the start of function header.
> A function name to uniquely identify it.
> Parameters (arguments). They are optional.
> A colon (:) to mark the end of function header.
> Optional documentation string (docstring) to describe what the function does.
> One or more valid python statements that make up the function body. 
  Statements must have same indentation level (usually 4 spaces).
> An optional return statement to return a value from the function.
"""

def greet(name):
    """Function greet:
    docstring goes here
    print(function_name.__doc___) to see what is written here
    Usually write helpful things to understand the function
    This function greets to the person passed in as parameter"""
    
    print("Hello, " + name + ". Good morning!")
    return None #Optional, if not specified, it returns None!

#----------------------
#Using Return option in the function
def number_to_K(num):
    """This function converts a large number into a condensed format"""
    CondensedNumber = str(round(num/1000)) + "K"
    return CondensedNumber

# when a function returns values you call it by using a variable 
# such as a = number_to_k(num)
    
#----------------------
"""SCOPE and LIFETIME of variables"""
def my_func():
    x = 10 
    print("Value inside function:",x)
    
x = 20 #This is the value outside my_func, not altered by value inside
my_func()
print("Value outside function:",x)

#----------------------
#GLOBAL VARIABLE
x = 100 #Outside definition
def foo():
    global x #Required to operate on x defined outside the function
    x+=1
    print("x inside :", x)

foo()
print("x outside:", x)
#----------------------

"""PYTHON FUNCTIONS: DEFAULT ARGUMENT"""
def greetmsg(name, msg = "Good morning!"):
    """This function greets to the person with the provided message.
    If message is not provided, it defaults to "Good Morning!
    """
    print("Hello",name + ', ' + msg)

# an argument is a defualt argument when you assign 
# value to variable in function definition
"""
> In greetmsg, name is a MANDATORY parameter, while msg is optional since
it has a default value.
> Any number of arguments in a function can have a default value
> But once we have a default argument, all the arguments to its right
must also have default values.
"""
#----------------------
"""OPTIONAL: ANONYMOUS FUNCTIONS"""
#Lambda
#Map
#Source: https://www.programiz.com/python-programming/anonymous-function
#----------------------


















