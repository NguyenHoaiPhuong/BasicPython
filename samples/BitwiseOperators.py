#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:07:41 2019

@author: akagi
"""

def exec():    
    print('------------ Bitwise Operators --------------')    
    
    a = 0b00111100
    b = 0b00001101
    print('a =', a, ', b =', b)
    print('a =', bin(a), ', b =', bin(b))
    
    # And
    print('------------ And --------------')
    c = a&b
    print(c)
    print(bin(c))
            
    # Or
    print('------------ Or --------------')
    c = a|b
    print(c)
    print(bin(c))
    
    # Xor
    print('------------ Xor --------------')
    c = a^b
    print(c)
    print(bin(c))    
    
    # Not
    print('------------ Not --------------')
    c = ~a
    print(c)
    print(bin(c))
    
    # Left shift
    print('------------- Left shift -------------')
    c = a << 2
    print(c)
    print(bin(c))
    
    # Right shift
    print('------------- Right shift -------------')
    c = a >> 2
    print(c)
    print(bin(c))