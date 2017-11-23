'''
Created on Sep 12, 2017

@author: Mark
'''
from cs115 import map, reduce
import math

def tower(n):
    if (n == 0):
        return 1
    return 2 ** tower(n - 1)

#print(tower(4))

def tower_reduce(n):
    def power(x, y):
        return x ** y
    return reduce(power, [2] * n)

def length(lst):
    if (lst == []):
        return 0
    return 1 + length(lst[1:])

#grab last Element
#add to list
#subtract from list

def member(x, lst):
    if(lst == []):
        return False
    if(x == lst[0]):
        return True
    return member(x, lst[1:])

def prime(n):
    """return whether or not an integer is prime"""
    possible_divisors = range(2, int(math.sqrt(n)) + 1)
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0

def primes(n):
    """returns a list of primes in the range [2, n] computed via the sieve
    of Eratosthenes."""
    
    def sieve(lst):
        if(lst) == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n + 1))

def fib(n):
    if(n <= 1):
        return n
    return fib(n - 1) + fib(n - 2)
#tree recursion occurs when the pending operation for the recursive call is another recursive call.

#use it or lose it strategy


    