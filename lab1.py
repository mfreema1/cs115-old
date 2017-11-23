'''
Created on Sep 7, 2017

@author: Mark
I pledge my honor that I have abided by the Stevens Honor System
'''
import cs115
from math import e as e_constant, factorial


"""return the reciprocal of a number as a float"""
def inverse(n):
    return float(1/n)

"""sum the Taylor expansion of a natural number"""
def e(n):
    return 1 + sum(map(inverse, map(factorial, range(1, n + 1))))

"""find error between above `e()` function and base of natural logarithm e"""
def error(n):
    return abs(e_constant - e(n))