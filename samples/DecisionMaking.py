#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  22 10:06:23 2019

@author: akagi
"""

def IfStatement():
    print("if statement")
    
    var1 = 100
    if var1:
       print("1 - Got a true expression value")
       print(var1)
    
    var2 = 0
    if var2:
       print("2 - Got a true expression value")
       print(var2)
    print("Good bye!")
    
def IfElseStatement():
    print("if else statement")
    
    var1 = 100
    if var1:
       print("1 - Got a true expression value")
       print(var1)
    else:
       print("1 - Got a false expression value")
       print(var1)
    
    var2 = 0
    if var2:
       print("2 - Got a true expression value")
       print(var2)
    else:
       print("2 - Got a false expression value")
       print(var2)
    
    print("Good bye!")
    
def ElifStatement():
    print("elif statement")
    
    var = 100
    if var == 200:
       print("1 - Got a true expression value")
       print(var)
    elif var == 150:
       print("2 - Got a true expression value")
       print(var)
    elif var == 100:
       print("3 - Got a true expression value")
       print(var)
    else:
       print("4 - Got a false expression value")
       print(var)
    
    print("Good bye!")
    
def NestedIfStatement():
    print("nested if statement")
    
    var = 100
    if var < 200:
       print("Expression value is less than 200")
       if var == 150:
          print("Which is 150")
       elif var == 100:
          print("Which is 100")
       elif var == 50:
          print("Which is 50")
       elif var < 50:
          print("Expression value is less than 50")
    else:
       print("Could not find true expression")
    
    print("Good bye!")