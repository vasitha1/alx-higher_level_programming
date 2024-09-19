#!/usr/bin/python3

def weight_average(my_list=[]):
    total_weight = 0
    weighted_score = 0

    for score, weight in my_list:
        total_weight += weight
        weighted_score += score * weight

    if total_weight == 0:
        return 0

    return weighted_score / total_weight
