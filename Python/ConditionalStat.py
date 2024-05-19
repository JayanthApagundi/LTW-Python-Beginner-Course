# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:12:37 2024

@author: Jayanth Apagundi
"""

# Conditional Statements

a=13
b=15
c=10

# simple if 
if a>b:
    print("Heyyy")
    print("Heyyyyyy")
    print("Byeeeee")
    
# simple if and else 
if a>b:
    print("Yes")
else:
    print("No")
    
# if else-if 
if b>c:
    print("Okay")
elif a==c:
    print("Hmmm")
else:
    print("Nope")
    
  
# + / x - % -> Arthematic Operators
# > < >= <= == != -> Comparsion Operator   
# Logical Operators -> AND, OR - We use them to combine conditions 

""" true-1 false-0
       1     0       0
       0     1       0
       0     0       0
       1     1       1"""
if a>b and b>c: 
    print("Both conditions true")

""" 1    0     1
    0    1     1
    0    0     0
    1    1     1"""
if a>b or b==c:
    print("Atleast one condition is true ")
    

""" 
a=5
b=3
c=4 
"""
# Nested if-else 
if a>b:
    print("Yes, a is greater than b")
    if a>c:
        print("Yes, a is grater than b and c")
    else:
        print("No, a is just greater than b")
else:
    print("No, a is not even greater than b")
    











    

