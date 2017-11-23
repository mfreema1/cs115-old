'''
Created on Sep 28, 2017
@author: Mark Freeman
I pledge my honor that I have abided by the Stevens Honor System
'''
def knapsack(capacity, itemList):
    """Returns the highest value  of items, given a set of capacities and associated values, that can fit in a given capacity"""
    def knapsackHelper(capacity, itemList, itemsSoFar, accumValue):
        """Helper function to the knapsack function that keeps track of each item in the knapsack as well as the accumulated value of the items"""
        if capacity == 0 or itemList == []:
            return [accumValue, itemsSoFar]
        if capacity - itemList[0][0] >= 0:
            use_it = knapsackHelper(capacity - itemList[0][0], itemList[1:], itemsSoFar + [itemList[0]], accumValue + itemList[0][1])
            lose_it = knapsackHelper(capacity, itemList[1:], itemsSoFar, accumValue)
            if(use_it[0] > lose_it[0]):
                return use_it
            return lose_it
        return knapsackHelper(capacity, itemList[1:], itemsSoFar, accumValue)
    
    return knapsackHelper(capacity, itemList, [], 0)


