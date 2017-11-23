'''
Created on Sep 14, 2017

@author: Mark
'''

def power(x, y):
    if(y == 0):
        return 1
    return x * (power(x, y - 1))

def power_tail(x, y):
    def power_tail_helper(x, y, accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, accum * x)
    return power_tail_helper(x, y, 1)

def mystery(n):
    return m_help(n,0)

def m_help(n,r):
    if n == 0:
        return r
    return m_help(n // 10, r * 10 + n % 10)

def my_map(f, L):
    if(L == []):
        return []
    return [f(L[0])] + my_map(f, L[1:])

def my_reduce(f, lst):
    
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(lst[0]], accum))
    
    if lst == []:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])

"""a lambda function is simply an anonymous function.  It has no name."""
#filter(lambda x: x % 2 == 1, lst)