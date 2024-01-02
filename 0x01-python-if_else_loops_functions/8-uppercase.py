#!/usr/bin/python3

def uppercase(str):
    upper_word = ""
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            upper_word += chr(ord(str[i]) - 32)
        else:
            upper_word += str[i]
    print(upper_word)
