#!/usr/bin/python3

def max_integer(my_list=[]):

    maxi = 0
    for item in my_list:
        if item > maxi:
            maxi = item
    return (maxi)
