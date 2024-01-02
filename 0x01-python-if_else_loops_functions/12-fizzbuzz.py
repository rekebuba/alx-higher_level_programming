#!/usr/bin/env python3

def fizzbuzz():
    for i in range (0, 101):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 5 == 0 == i % 3:
            print("FizzBuzz")
        else:
            print(f"{i}", end=" ")
