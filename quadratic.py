"""
Mark Freeman mfreema1
I pledge my honor that I have abided by the Stevens Honor System.
"""
class QuadraticEquation(object):
    """class modeling the quadratic equation"""
    def __init__(self, a, b, c):
        """constructor for a quadratic equation object.  It takes in three variables to be coefficients of the equation."""
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")

        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    @property
    def a(self):
        """returns the first coefficient"""
        return self.__a

    @property
    def b(self):
        """returns the second coefficient"""
        return self.__b

    @property
    def c(self):
        """returns the third coefficient"""
        return self.__c

    def discriminant(self):
        """returns the b squared minus 4ac part of the quadratic equation"""
        return self.__b * self.__b - 4 * self.__a * self.__c

    def root1(self):
        """returns the first real root of the quadratic equation"""
        if self.discriminant() < 0:
            return None
        return (-self.__b + self.discriminant() ** .5)/(2 * self.__a)

    def root2(self):
        """returns the second real root of the quadratic equation"""
        if self.discriminant() < 0:
            return None
        return (-self.__b - self.discriminant() ** .5)/(2 * self.__a)

    def aTerm(self, a):
        """helper function for the str method to print the first term"""
        if a == 1.0:
            return 'x^2'
        if a == -1.0:
            return '-x^2'
        return str(a) + 'x^2'

    def bTerm(self, b):
        """helper function for the str method to print the second term"""
        if b < 0:
            if b == -1.0:
                return ' - x'
            return ' - ' + str(abs(b)) + 'x'
        if b == 0:
            return ''
        if b == 1.0:
            return ' + x'
        return ' + ' + str(abs(b)) + 'x'

    def cTerm(self, c):
        """helper function for the str method to print the third term"""
        if c < 0:
            return ' - ' + str(abs(c))
        if c == 0:
            return ''
        return ' + ' + str(abs(c))

    def __str__(self):
        """converts the object to a readable string"""
        return self.aTerm(self.__a) + self.bTerm(self.__b) + self.cTerm(self.__c) + ' = 0'
