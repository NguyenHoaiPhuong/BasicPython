# -*- coding: utf-8 -*-

def WhileLoop():
    print("while loop")
    
    var = 0
    while var < 9:
        print(var)
        var += 1

def InfiniteWhileLoop():
    print("infinite loop")
    
    var = 1
    while var == 1:
        num = input("Enter an integer number: ")
        try:
            val = int(num)
            print(val)
        except ValueError:
            print(num, "is not an integer")
            break

def WhileElseLoop():
    print("while else loop")
    
    var = 0
    while var < 5:
        print(var)
        var += 1
    else:
        print(var, "is greater than or equal to 5")
        
def ForLoop():
    print("for loop")
    
    for letter in "pythons":
        print("Current letter:", letter)
        
    fruits = ["banana", "apple", "orange"]
    for fruit in fruits:
        print(fruit)
        
    for i in range(5):
        print(i)
        
def ForElseLoop():
    for num in range(10, 20):
        for i in range(2, num):
            if num % i == 0:
                print(num, "=", i, "*", int(num/i))
                break
        else:
           print(num, "is a prime number")