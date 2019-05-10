#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:06:23 2019

@author: akagi
"""

# Assigning Values to Variables
def SingleAssignValueToVariable():
    print("Single assign value to variable")

    print('-------------- x = 1 -----------------')
    x = 1
    print(type(x))    
    
    print('--------------- x = 1.0 ----------------')
    x = 1.0
    print(type(x))    
    
    print('--------------- x = 1 + 2j ----------------')
    x = 1 + 2j
    print(type(x))    
    
    print('-------------- x = John -----------------')
    x = 'John'
    print(type(x))    

    print("\n")


# Multiple Assignment
def MultipleAssignValueToVariable():
    print("Multiple assign value to variable")

    print('-------------- a = b = c = 1 -----------------')
    a = b = c = 1
    print('a =', a, ', b =', b, ', c =', c)
    
    print('--------------- a, b, c = 1, 2, John ----------------')
    a, b, c = 1, 2, 'John'
    print('a =', a, ', b =', b, ', c =', c)
    
    print('-------------------------------')
    
    print('Number Type Conversion:')
    x = 2.7
    y = 4.5
    print("x = ", x)
    print("y = ", y)    
    print("int(x) = ", int(x))
    print("str(x) = ", str(x))    

    a = complex(x)
    print('complex(x) = ', a)
    
    a = complex(x, y)
    print('complex(x, y) = ', a)
    
    print('-------------------------------')
    print("\n")


# Delete variable
def DeleteVariable():
    print("Delete Variable")

    x = 2.0
    y = x
    print('x =', x, ', y =', y)
    print('Address of x:', hex(id(x)), ', address of y:', hex(id(y)))
    del x
    # print('Address of x:', hex(id(x))) error
    print('Address of y:', hex(id(y)))
