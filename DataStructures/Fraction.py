"""
Created on: 15-Mar-2018
Created by: Maneesh D
"""


def _gcd(num1, num2):
    while num1 % num2 != 0:
        old_num1 = num1
        old_num2 = num2
        num1 = old_num2
        num2 = old_num1 % old_num2
    return num2


def _fp_almost_equal(x, y, delta=1e-10):
    return abs(x - y) < delta


class Fraction(object):

    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError
        common = _gcd(num, den)
        self.numerator = num // common
        self.denominator = den // common

    def __str__(self):
        neg_flag = True
        if (self.numerator < 0 and self.denominator < 0) or (self.numerator > 0 and self.denominator > 0) or (self.numerator == 0):
            neg_flag = False
        if self.numerator == 0:
            return "0"
        num_str_rep = str(self.numerator).replace("-", "")
        den_str_rep = str(self.denominator).replace("-", "")
        str_rep = "-" if neg_flag else ""
        if self.numerator == self.denominator:
            str_rep += num_str_rep
        else:
            str_rep += num_str_rep + "/" + den_str_rep
        return str_rep

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __floordiv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        num1 = self.__float__()
        num2 = other.__float__()
        return _fp_almost_equal(num1, num2)

    def __le__(self, other):
        num1 = self.__float__()
        num2 = other.__float__()
        return num1 <= num2

    def __lt__(self, other):
        num1 = self.__float__()
        num2 = other.__float__()
        return num1 < num2

    def __ge__(self, other):
        num1 = self.__float__()
        num2 = other.__float__()
        return num1 >= num2

    def __gt__(self, other):
        num1 = self.__float__()
        num2 = other.__float__()
        return num1 > num2

    def __float__(self):
        return self.numerator / self.denominator
