'''
Created on Oct 3, 2017

@author: Mark
'''
#memoization
#1) if key is in the memo, return the value associated with the key.
#2) Do work! Use recursion to compute your answer, but store the result in a local variable.
#3) Put the result in the memo and then return the result.

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_memo(n):
    def fib_helper(n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
        memo[n] = result
        return result
    return fib_helper(n, {})

def LCS(S1, S2):
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

#print(LCS("ghrafhelafea", "feahughejaljf")) # this will also fail.

def LCS_memo(S1, S2):
    def LCS_helper(S1, S2, memo):
        if(S1, S2) in memo:
            return memo[(S1, S2)]
        if S1 == '' or S2 == '':
            result = 0
        elif S1[0] == S2[0]:
            result = 1 + LCS_helper(S1[1:], S2[1:], memo)
        else:
            result = max(LCS_helper(S1, S2[1:], memo), LCS_helper(S1[1:], S2, memo))
        memo[(S1, S2)] = result
        return result
    
print(LCS_memo("efahkghelafe", "feahfuehalkfhl"))
    

print(fib_memo(900)) # this wont work, it takes too long to compute