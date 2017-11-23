"""I pledge my honor that I have abided by the Stevens Honor System.
mfreema1
Mark Freeman"""
from cs5png import *

def mult(c, n):
    """multiples two numbers using addition and a loop"""
    result = 0
    for x in range(n):
        result += c
    return result

def update(c, n):
    """updates a number using the mandelbrot set equation"""
    z = 0
    for x in range(n):
        z = z ** 2 + c
    return z

def inMSet(c, n):
    """ inMSet takes in
     c for the update step of z = z**2+c
     n, the maximum number of times to run that step
     Then, it should return
     False as soon as abs(z) gets larger than 2
     True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    for x in range(n):
        if abs(z) > 2:
            return False
        z = z ** 2 + c
    return True

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    # changes the grid from dots to lines
    if col%10 == 0 and row%10 == 0:
        return True
    else:
        return False
def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
     # create a loop in order to draw some pixels

    for col in range(width):
         for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
     # we looped through every image pixel; we now write the file
    image.saveFile()

def scale(pix, pixelMax, floatMin, floatMax):
    """ scale takes in
     pix, the CURRENT pixel column (or row)
     pixMax, the total # of pixel columns
     floatMin, the min floating-point value
     floatMax, the max floating-point value
     scale returns the floating-point value that
     corresponds to pix
     """
    return (1.0*pix / pixelMax) * (floatMax - floatMin) + floatMin

def mset():
    """ a function to demonstrate how
     to create and save a png image
     """
    n = 25
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
         # here is where you will need
         # to create the complex number, c!
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y * 1j
            if inMSet( c, n ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
mset()
