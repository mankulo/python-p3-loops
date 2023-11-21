#!/usr/bin/env python3

def happy_new_year():
    
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!") 

    pass

def square_integers(int_list):
    
    squared_list = [element * element for element in int_list]

    return squared_list
    

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



