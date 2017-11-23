'''
Created on Oct 5, 2017

@author: Mark
'''
import turtle

def square_spiral(walls):
    def square_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(distance + initial * ( count % 2 == 0), initial, count)
    square_spiral_helper(20, 20, 0)

square_spiral(30)

#distance - length of current wall
#initial - length of the first wall on the inner part of the spiral