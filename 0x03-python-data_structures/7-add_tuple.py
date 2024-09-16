#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_c = [0, 0]

    for number in range(2):
        if number < len(tuple_a):
            tuple_c[number] += tuple_a[number]
        if number < len(tuple_b):
            tuple_c[number] += tuple_b[number]

    return (tuple(tuple_c))
