#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:07:41 2019

@author: akagi
"""

a = 0b00111100
b = 0b00001101
print('a =', a, ', b =', b)

print('--------------------------')

# And
c = a&b
print(c)

print('--------------------------')

# Or
c = a|b
print(c)

print('--------------------------')

# Xor
c = a^b
print(bin(c))

print('--------------------------')

# Not
c = ~a
print(c)

print('--------------------------')

# Left shift
c = a << 2
print(c)

print('--------------------------')

# Right shift
c = a >> 2
print(c)