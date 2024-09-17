#!/usr/bin/python3

def max_integer(my_list=[]):

    if  len(my_list) == 0:
        return
    maxi = 0
    for item in my_list:
        if item > maxi:
            maxi = item
    return (maxi)
