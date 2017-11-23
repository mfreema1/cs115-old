#
# life.py - Game of Life lab
#
# Name: Mark Freeman mfreema1
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#
import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for _ in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """returns a board"""
    brd = []
    for row in range(height):
        brd += [createOneRow(width)]
    return brd

import sys
def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width, height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width, height):
    """make a board of inner cells"""
    A = createBoard(width, height)
    for row in range(height):
        if row == 0 or row == height - 1:
            for col in range(width):
                A[row][col] = 0
        else:
            for col in range(width):
                if col == 0 or col == width - 1:
                    A[row][col] = 0
                else:
                    A[row][col] = 1
    return A

def randomCells(width, height):
    """make a board of random cells"""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            A[row][col] = random.choice([0, 1]) # randomly initialize

    for row in range(height): # handle cleaning up the edge
        if row == 0 or row == height - 1:
            for col in range(width):
                A[row][col] = 0
        else:
            for col in range(width):
                if col == 0 or col == width - 1:
                    A[row][col] = 0
    return A

def copy(oldA):
    """make a deep copy"""
    A = createBoard(len(oldA), len(oldA[0]))
    for row in range(len(A)):
        for col in range(len(A[0])):
            A[row][col] = oldA[row][col]
    return A

def innerReverse(A):
    """reverse the inner cells of a board"""
    B = copy(A)
    for row in range(len(B)):
        for col in range(len(B[0])):
            if B[row][col] == 0:
                B[row][col] = 1
            else:
                B[row][col] = 0

    for row in range(len(B)): # handle cleaning up the edge
        if row == 0 or row == len(B) - 1:
            for col in range(len(B[0])):
                B[row][col] = 0
        else:
            for col in range(len(B[0])):
                if col == 0 or col == len(B[0]) - 1:
                    B[row][col] = 0
    return B

def next_life_generation( A ):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    def countNeighbors(row, col, A):
        """returns the number of live neighbors of a block"""
        count = 0
        if A[row + 1][col] == 1: # right
            count += 1
        if A[row][col + 1] == 1: # up
            count += 1
        if A[row - 1][col] == 1: # left
            count += 1
        if A[row][col - 1] == 1: # down
            count += 1
        if A[row + 1][col + 1] == 1: # up-right
            count += 1
        if A[row - 1][col + 1] == 1: # up-left
            count += 1
        if A[row - 1][col - 1] == 1: # down-left
            count += 1
        if A[row + 1][col - 1] == 1: # down-right
            count +=1
        return count

    newA = copy(A)
    for row in range(len(A))[1:-1]:
        for col in range(len(A[0]))[1:-1]:
            if(countNeighbors(row, col, A) < 2): # die of loneliness
                newA[row][col] = 0
            if(countNeighbors(row, col, A) > 3): # die of overcrowding
                newA[row][col] = 0
            if(countNeighbors(row, col, A) == 3 and A[row][col] == 0): #bring to life
                newA[row][col] = 1
    return newA
