# -*- coding: utf-8 -*-
"""
Created on  Wed Apr 10 01:10:20 2019
@uthor: Aveedibya Dey
"""
# GENERATORS - Creates Iterator objects (since Python3) which support lazy evaluation
# Lazy evaluation evaluates only when asked for, consuming less memory
# ----------

def firstn(n):
   '''
   Generate first 'n' whole numbers
   Defining a Generator function, note how it uses "yield" and not return
   '''
   num = 0
   while num < n:
       yield num
       num += 1
       
# Create a generator object from the above function
a = firstn(5)

print(a) # <generator object firstn at 0x124c205e8> ... 'a' is an iterator

# One way to get values out of 'a' ... note how it will give you values only when you ask for it
next(a) # 0
next(a) # 1
#...
next(a) # 4
next(a) # gives StopIteration error

# alternate way of printing the output
list(a) # [0, 1, 2, 3, 4]

# alternate way of printing the output
for i in a:
    print(i)
# 0
# 1
# 2
# 3
# 4
# ----------

def add(x, y):
    '''
    Simple function to add two values
    '''
    return x + y

# LAMBDA Function - One line functions
# ----------
add_lambda = lambda x, y : x + y  

print(add_lambda(2, 3))

# Advantages of lambda function can be seen when used with other functions 
# such as Map, Filter

# MAP Function - applies a function to an iterable, such as a list
# Generic syntax of map function - map(function, iterable1, iterable2, ...)
# ----------

list1 = [1,2,3,4,5]
# I want to square each element in this list
map(lambda x: x ** 2, [1,2,3]) # Output: <map at 0x124cd5e80> ... an iterator object

list(map(lambda x: x ** 2, [1,2,3])) # Output: [1, 4, 9]
# You can use again any way you want to print the output, same as shown in generator above

# Map function example using two iterables, note how the order of x, y matters
list(map(lambda x, y: y/x, [2,3,4], [20,30,40]))
# Output: [10.0, 10.0, 10.0]


# FILTER Function - Similar to map, but function needs to be a boolean check,
# and only 1 iterable is accepted
# Note: if the function doesn't do boolean check, then there will be no filtering
# ----------
a = [1, 2, 3, 4, 5, 6]

# Creates a filter object, again an iterator
filter(lambda x : x % 2 == 0, a) # Output: <filter at 0x124cdf470>

# Force convert to list, see how the lambda function has a boolean true/false check
# Filter function returns the result only where boolean check is True
list(filter(lambda x : x % 2 == 0, a)) # Output: [2, 4, 6]


# ZIP Function - Combine 2 or more iterables
# ----------
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = zip(list_a, list_b) # Output: <zip at 0x124ce3208> ... again an iterator

# Force convert to list
list(zipped_list) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# Note how certain values from list_b are ignored, as list_a only has 3 elements

#Unzip the zipped list, note you may need to zip it before unzipping
unzip_a, unzip_b = zip(*zipped_list)

print(unzip_a) # Output: (1, 2, 3)
print(unzip_b) # Output: ('a', 'b', 'c')

# -----
# Reference: 
#  1. https://medium.com/@happymishra66/lambda-map-and-filter-in-python-4935f248593
#  2. https://blog.usejournal.com/zip-in-python-48cb4f70d013
# -----