'''
Created on Sep 18, 2017

@author: Mark
'''
# this is a specific genre of algorithms called use it or lose it.
from cs115 import map

def powerset(lst):
    """returns the power set of the list, that is, the set of all subsets of the list"""
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

print(powerset(['a', 'b', 'c']))

def powerset(lst):
    """returns the power set of the list, that is, the set of all subsets of the list"""
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

print(powerset(['a', 'b', 'c']))