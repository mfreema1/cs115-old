'''
Created on 10/12/17
@author:   Mark Freeman
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd. The base 2 representation
    of 42 is 101010'''
    return n % 2 == 0

#I think that for an odd number, the right most digit will be 1.  For an even number,
# the right most digit should be 0.

#When we eliminate the right most bit, we are halving the value of the number at least.
#If it was a 1, then we halved and subtracted one.  Otherwise, we just halved it.

#We would just tack on a number to the end of Y.  If N is odd, then we tack on a 1.
#otherwise, we tack on a 0.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + '0'
    else:
        return numToBinary(n // 2) + '1'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '0':
        return 2 * binaryToNum(s[:-1])
    elif s[-1] == '1':
        return  1 + 2 * binaryToNum(s[:-1])

def pare(s):
    """adjusts the length of a binary number to be 8 bits, cutting off an overflow)"""
    if len(s) == 8:
        return s
    if len(s) > 8:
        return pare(s[1:])
    if len(s) < 8:
        return pare('0' + s)

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''

    return pare(numToBinary(1 + binaryToNum(s)))
        
def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        return s
    if n > 0:
        return count(increment(s), n - 1)
    
#the ternary representation of 59 is 2012 using the same method of division and remainders
#as used in binary
    
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n % 3 == 0:
        return numToTernary(n // 3) + '0'
    if n % 3 == 1:
        return numToTernary(n // 3) + '1'
    if n % 3 == 2:
        return numToTernary(n // 3) + '2'        

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '0':
        return 3 * ternaryToNum(s[:-1])
    elif s[-1] == '1':
        return 1 + 3 * ternaryToNum(s[:-1])
    elif s[-1] == '2':
        return 2 + 3 * ternaryToNum(s[:-1])