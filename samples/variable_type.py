#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:06:23 2019

@author: akagi
"""

# Assigning Values to Variables
def SingleAssignValueToVariable():
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


# Multiple Assignment
def MultipleAssignValueToVariable():
    print('-------------- a = b = c = 1 -----------------')
    a = b = c = 1
    print('a =', a, ', b =', b, ', c =', c)    
    
    print('--------------- a, b, c = 1, 2, John ----------------')
    a, b, c = 1, 2, 'John'
    print('a =', a, ', b =', b, ', c =', c)    
    
    # Number Type Conversion
    print('--------------- x = 2.3 ----------------')
    x = 2.3
    print("int(x) = ", int(x))
    print("str(x) = ", str(x))    
    
    
    x = 2.3
    y = 4.5
    a = complex(x)
    print(a)
    
    print('-------------------------------')
    
    a = complex(x, y)
    print(a)
    
    print('-------------------------------')


# Delete variable
def DeleteVariable():
    x = 2.0
    y = x
    print('x =', x, ', y =', y)
    print('Address of x:', hex(id(x)), ', address of y:', hex(id(y)))
    del x
    # print('Address of x:', hex(id(x))) error
    print('Address of y:', hex(id(y)))
