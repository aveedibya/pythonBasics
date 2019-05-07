# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 12:34:20 2018
@author: Aveedibya Dey
"""
"""PYTHON FLOW CONTROL"""
#----------------------
#IF...ELSE Satements
#----------------------
num = 3.4

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#----------------------
#FOR Loop
#----------------------
# Program to find the sum of all numbers stored in a list
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0
# iterate over the list
for i in numbers:
	sum = sum + i

#----------Another way to execute For Loop
# Output: The sum is 48
print("The sum is", sum)

# Program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])


#----------Another way to execute For Loop using Enumerate()
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list):
    print(c, value)
"""
enumerate gives both the indices 
and the values in two variables
and in this case you declare 2 variables 
first one takes index, second takes value on index
"""
 
    
#Optional argument for enumerate... fix the counter    
for c, value in enumerate(my_list, 1):
    print(c, value)
#Counter will start from 1, all values will be shown still


#----------------------
#WHILE LOOP
#----------------------
n = 10
i = 1

while i <= n:
    i = i+1    # update counter
    print("The current value of i is",i)

# print the sum
print("The sum is", sum)

#----------------------CONTINUE STATEMENT
for val in "string":
    if val == "i":
        continue
    print(val)

#----------------------BREAK STATEMENT
for val in "string":
    if val == "i":
        break
    print(val)

#----------------------
"""PYTHON ARBITRARY ARGUMENTS - USES FOR LOOP"""
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")
"""

in order to take input
use var = input ("enter name/variable")
the message will display
and will allow you to add value
then display if you print var it has input