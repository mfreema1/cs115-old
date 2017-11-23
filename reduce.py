'''
Created on Sep 7, 2017

@author: Mark
'''
from cs115 import range, map, reduce

def span(list):
    return reduce(max, lst) - reduce(min, lst)
# reduce repeatedly applies a function to a list, continually shortening the list using that function until it gets one value

def add(a, b):
    return a + b

def gauss(n):
    #return sum(range(1, n + 1))
    return reduce(add, range(1, n + 1))

def sqr(x):
    return x * x

def sumOfSquares(n):
    return reduce(add, map(sqr, range(1, n + 1)))

list_of_strings = ['hello', 'my', 'name', 'is', 'brian']

def multiply(a, b):
    return a * b

list_of_ints = [1, 2, 3, 4, 5]
def multiplyLists(lst):
    return reduce(multiply, lst)

print(map(len, list_of_strings))

print(gauss(5))
    