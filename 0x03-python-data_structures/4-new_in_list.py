#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    my_list_copy = []

    for item in range(len(my_list) - 1):

        if item == idx:
            my_list_copy.append(element)
        else:
            my_list_copy.append(my_list[item])

    return (my_list_copy)
