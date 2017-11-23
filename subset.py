'''
Created on Sep 19, 2017

@author: Mark
'''
def subset(target, lst):
    if target == 0:
        return True
    if lst == []:
        return False
    if (target - lst[0] >= 0):
        return subset(target - lst[0], lst[1:])
    return subset(target, lst[1:])

def subset_in_class(target, lst):
    if target == 0:
        return True
    if (lst == []):
        return False
    use_it = subset(target - lst[0], lst[1:])
    lose_it = subset(target, lst[1:])
    return use_it or lose_it
    
    # 'and' and 'or' are what we call short circuit operators in python.  Similar to Java.
    # it doesn't bother calculating the other side of the operand if the result can be deduced
    # from the first operand
    
    def subset_with_values(target, lst):
        """determines whether or not it is possible to create the target sum using values
        in the list.  The function returns a tuple of exactly two items.  The first is a boolean that indicates whether
        or not the sum is possible.  The second element in the tuple is a list of all values that make up the 
        target sum"""
        
        #tuples are dimensionless and not mutable, meaning they cannont be modified
    
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])