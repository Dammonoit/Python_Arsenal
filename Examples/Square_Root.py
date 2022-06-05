# -*- coding: utf-8 -*-
"""
Created by :-
    Dharmendra Choudhary
Problem : - In the program below, find the square root of a number using exponent operator and cmath module.

"""
def Using_Math_Module(a):
    return math.sqrt(a)

def Using_Exponential_Method(b):
    return b**0.5


import math
#Python has a below built-in module that you can use for mathematical tasks for complex numbers.
import cmath

num_p = int(input("Enter the positive number: "))
num_n = int(input("Enter the negative number: "))
num_c = 1+2j
num_c_sqrt = cmath.sqrt(num_c)
print("The squareoot of Positive Number {0} using Math Module is {1:0.3f}".format(num_p,Using_Math_Module(num_p)))
print("The squareoot of Negative Number {0} using Exponential Method is {1:0.3f}".format(num_n,Using_Exponential_Method(abs(num_n))))
print("The squareoot of Complex Number {0} using Math Module Method is {1:0.3f}+{2:0.3f}j".format(num_c,num_c_sqrt.real,num_c_sqrt.imag))
