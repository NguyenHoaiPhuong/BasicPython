#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:20:01 2019

@author: akagi
"""
x, y, z = 1, 2, 3

# Logical AND
if x < y and y < z:
    print('Increase gradually')
else:
    print('Do not increase gradually')

# Logical OR
if x < y or y > z:
    print('x < y or y > z')

# Logical NOT
if not x > y:
    print('x <= y')