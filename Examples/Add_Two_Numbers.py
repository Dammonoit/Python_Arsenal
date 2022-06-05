# -*- coding: utf-8 -*-
"""
Created by :-
    Dharmendra Choudhary
Problem : - In the program below, we've used the + operator to add two numbers.
"""

def add(a,b):
    return a+b

a=int(input("Enter first number "))
b=int(input("Enter second number "))

print("Addition of {0} and {1} is {2}".format(a,b,add(a,b)))