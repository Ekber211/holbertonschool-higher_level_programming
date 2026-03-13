#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_integers = set(my_list)
    for num in uniq_integers:
        result += num
    return result
