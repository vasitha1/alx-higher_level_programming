#!/usr/bin/python3

def get_max(roman_num):
    c = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    d = dict(map(lambda x: (x, c.get(x)), roman_num))
    maximum_val_key = max(d)
    return maximum_val_key

def add_num_val(roman_num, number, max_val_key)
    for i in range(len(roman_num) - 1):
        if (roman_num[i] == maximum_val_key)
            first = i
            number += c.get(roman_num[i])
            if roman_num[i + 1] != maximum_val_key
                break
    return [number, first, i]
    

def roman_to_int(roman_string):
    c = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}

    roman_num = list(roman_string)
    maximum_val_key = get_max(roman_num)
    number = 0

    while maximum_val_key != "I":
        if max
        number, first, sec = add_num_val(roman_num, number, max_val_key)
        if first != 0
            value_before, first, second = add_num_val(roman_num[: 
        
