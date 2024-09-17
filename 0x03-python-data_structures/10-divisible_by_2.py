#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisible = []

    for item in my_list:

        number = abs(item)

        if number % 2 == 0:
            divisible.append(1)
        else:
            divisible.append(0)

    return (tuple(divisible))
