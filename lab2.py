"""
Mark Freeman
I pledge my honor that I have abided by the Stevens Honor System
"""
def add(x, y):

    """returns x added to y"""

    return x + y

def mult(x, y):

    """returns x multiplied by y"""

    return x * y

def dot(L, K):

    """returns the dot product of two vectors of the same shape"""

    if(L == [] or K == []): # assuming same shape
        return 0
    return add(mult(L[0], K[0]), dot(L[1:], K[1:]))

def explode(S):

    """returns a string as a list with elements length 1"""

    if(S == ''):
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):

    """returns the index of an element e in list L.  If element e is not in list L, returns length of list"""
    if(L == [] or L == ''):
        return 0
    if(L[0] == e):
        return 0
    return (1 + ind(e, L[1:]))

def removeAll(e, L):

    """returns a list with elements e removed from it"""

    if(L == []):
        return []
    if(e == L[0]):
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

def myFilter(f, L):

    """returns a filtered list L with elements for which function f returned true"""

    if(L == []):
        return []
    if(f(L[0])):
        return [L[0]] + myFilter(f, L[1:])
    return myFilter(f, L[1:])


def deepReverse(L):

    """return the reversed form of a list.  Inner lists are also reversed"""

    if(L == []):
        return []
    if(isinstance(L[-1], list)):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    return [L[-1]] + deepReverse(L[:-1])
