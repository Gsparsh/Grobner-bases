from __future__ import division
import random
import math

class mono:

    def __init__(self):
        """
        This function initializes a monomial to xyz


        """
        self.x = 0
        self.y = 0
        self.z = 0
        self.c = 0

    def getValues(self):
        """

        This function stores the input of one monomial

        """
        self.x = int(input('Enter power of x:'))
        self.y = int(input('Enter power of y:'))
        self.z = int(input('Enter power of z:'))
        self.c = int(input('Enter Coeff:'))

    def repr(self):
        """

        this function represents a monomial
        :return:         'x^1.0*y^1.0*z^1.0'

        """
        string = []
        if self.c == 0:
            string = str('0')
            return string
        if self.x == 0:
            if self.y == 0:
                if self.z == 0:
                    string = str('1')
                    return string
                else:
                    if self.c == 1:
                        string = '*z^' + str(self.z)
                    else:
                        string = str(self.c) + '*z^' + str(self.z)
                    return string
            else:
                if self.c == 1:
                    string = 'y^' + str(self.y) + '*z^'
                else:
                    string = str(self.c) + '*y^' + str(self.y) + '*z^'
                return string
        else:
            if self.c == 1:
                string = 'x^' + str(self.x) + '*y^' + str(self.y) + '*z^' + str(self.z)
            else:
                string = str(self.c) + '*x^' + str(self.x) + '*y^' + str(self.y) + '*z^' + str(self.z)
            return string

    def monoDiv(self, first, second):
        """
        This function returns the division of two monomials

        """
        if second.c == 0:
            self.x = 0
            self.y = 0
            self.z = 0
            self.c = 0
        else:
            self.x = first.x - second.x
            self.y = first.y - second.y
            self.z = first.z - second.z
            self.c = first.c / second.c

        return self

    def monoAdd(self, first, second):
        """

        This function returns the addition of two monomials

        """
        if first.x == second.x and first.y == second.y and first.z == second.z:
            self.x = first.x
            self.y = first.y
            self.z = first.z
            self.c = first.c + second.c
            return self
        else:
            print('It will result in Polynolmial')

    def monoSub(self, first, second):
        """
        This function returns the subtraction of two monomials

        """
        if first.x == second.x and first.y == second.y and first.z == second.z:
            self.x = first.x
            self.y = first.y
            self.z = first.z
            self.c = first.c - second.c
            return self
        else:
            print('It will result in Polynomial')

    def monoMult(self, first, second):
        """

        This function returns the multiplication of two monomials

        """
        self.x = first.x + second.x
        self.y = first.y + second.y
        self.z = first.z + second.z
        self.c = first.c * second.c
        return self

    def lcm(self, first, second):
        """

        This returns the greatest common divisor of two monomials
        :param first: 'x^2.0*y^2.0*z^2.0'
        :param second: 'x^1.0*y^1.0*z^1.0'

        :return: 'x^2.0*y^2.0*z^2.0'

        """
        if first.x >= second.x:
            self.x = first.x
        else:
            self.y = second.y

        if first.y >= second.y:
            self.y = first.y
        else:
            self.y = second.y

        if first.z >= second.z:
            self.z = first.z
        else:
            self.z = second.z

        m = math.gcd(first.c, second.c)
        if m != 0:
            if first.c != 0 and second.c != 0:
                self.c = (first.c * second.c) / m
            elif first.c != 0:
                self.c = first.c
            elif second.c != 0:
                self.c = second.c

        return self

    def gcf(self, first, second):
        """

                This returns the greatest common divisor of two monomials
                :param first: 'x^2.0*y^2.0*z^2.0'
                :param second: 'x^1.0*y^1.0*z^1.0'
                :return: 'x^1.0*y^1.0*z^1.0'

        """
        self.x = math.gcd(first.x, second.x)
        self.y = math.gcd(first.y, second.y)
        self.z = math.gcd(first.z, second.z)
        self.c = math.gcd(first.c, second.c)

        return self

    def is_divisible_by(self, other):
        """

        This functions returns a boolean value of True and False depending
        if the monomial is divisible by the other monomial

        ;:param self: 'x^2.0*y^2.0*z^2.0'
        :param other: 'x^1.0*y^1.0*z^1.0'

        :return: True

        """
        if self.x >= other.x and self.y >= other.y and self.z >= other.z:
            return True
        else:
            return False
