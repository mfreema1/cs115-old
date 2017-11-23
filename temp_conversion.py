'''
Created on Sep 5, 2017

@author: Mark
'''
from pip._vendor.pyparsing import line

"""
put functions at the top of the program
"""
def fahrenheit(celsius):
    """returns the input celsius degrees in fahrenheit"""
    return (celsius * (9/5) + 32);

def celsius(fahrenheit):
    """returns the input fahrenheit degrees in celsius"""
    return ((fahrenheit - 32) * (5/9));

"""
call the functions below their declaration in python
"""
c = float(input('Enter degrees in Celsius: '));
f = fahrenheit(c);

# you can print multiple items in one statement if you put a comma after each item
#it prints a space and then goes on to print the next item
print(c, 'C =', f, 'F');

# you can print this way too, but allowing exactly two decimal places
print('%.2f C = %.2f F' % ()); # the number following the %. is the number of deceimal places

f = float(input('Enter degrees in Fahrenheit: '))
c = celsius(f)
print(f, 'F =', c, 'C')
print('%.2f F = %.2f C' % (f, c))

"""
trying composition of functions
converting a fahrenheit temperature to celsius and back to fahrenheit should give you the original fahrenheit temperature
"""

print() #print by itself prints a new line
f = float(input('Enter degrees in fahrenheit: '));

# Use assert to check the return value is equal to the expected value
assert fahrenheit(celsius(f)) == f
# No output should be produced unless assertion fails

# the range function takes a subset of a list by element.  It will search through the list until it it hits the given value.
list = [0,1,2,3,4,5]
#three forms. range(stop), range(start, stop), and range(start, stop, step)

