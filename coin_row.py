'''
Created on Sep 25, 2017

@author: Mark
'''
def coin_row(lst):
    if lst ==  []:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values(lst):
    if lst == []:
        return [0, []]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:]) 
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it

def distance(first, second):
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0] == second[0]:
        distance(first[1:], second[1:])
    substitution = 1 + distance(first[1:], second[1:])
    deletion = 1 + distance(first[1:], second)
    insertion = 1 + distance(first, second[1:])
    return min(substitution, deletion, insertion)

# notice how we didn't compare the lst index 1 to the list index 0.  this might be
# obvious, but it can easily render a list index out of bounds exception.  A better way
# to do this is to use the max() function.  This way we don't access the next list index
# and can avoid getting index out of bounds exception. 

print(coin_row([1,2,3,4,5,6]))
print(coin_row_with_values([1,2,3,4,5,6]))

def fun(n):
    if n <= 1:
        print('bye')
        return
    fun(n - 1)
    print('hi')
    fun(n - 1)
    
print(fun(3))