"""
Mark Freeman
CS 115
lab3
I pledge my honor that I have abided by the Stevens Honor System.
"""

def change(amount, coins):
    """returns the minimum number of coins that can be used to dispense an amount with a given set of coin values"""
    def change_helper_method(change_to_go, current_coin_index):
        """helper method for the change method to keep track of the increment while moving through.
        This branches out, some will jump to infinity after dipping under, but the min function will eliminate those paths.
        The final line uses use-it or lose-it with a +1 increment to keep track of the number of coins needed."""
        if change_to_go == 0:
            return 0
        
        if current_coin_index < 0 or change_to_go < 0: #min function will eliminate infs, takes care of bad input
            return float('inf')
        
        return min(change_helper_method(change_to_go, current_coin_index - 1), 1 + change_helper_method(change_to_go - coins[current_coin_index], current_coin_index))#branch out
    return change_helper_method(amount, len(coins) - 1) #lines up length with index starting at 0