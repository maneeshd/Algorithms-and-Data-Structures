"""
Created on: 15-Mar-2018
Created by: Maneesh D
"""


def _gcd(num1: int, num2: int) -> int:
    """Get the GCD of the given two numbers"""
    while num1 % num2 != 0:
        old_num1 = num1
        old_num2 = num2
        num1 = old_num2
        num2 = old_num1 % old_num2
    return num2


def _fp_almost_equal(x: float, y: float, delta: float = 1e-10) -> bool:
    """Compares given two floating point numbers with delta compensation"""
    return abs(x - y) < delta


class Fraction:
    """Fraction Class"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Constructor for Fraction"""
        if denominator == 0:
            raise ZeroDivisionError
        common = _gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __str__(self):
        """String representation of the Fraction"""
        neg_flag = True
        if (self.numerator < 0 and self.denominator < 0) or (
            self.numerator > 0 and self.denominator > 0
        ):
            neg_flag = False
        if self.numerator == 0:
            neg_flag = False
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
        """Add this fraction with another fraction"""
        new_numerator = (self.numerator * other.denominator) + (
            other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Subtract the other fraction from this fraction"""
        new_numerator = (self.numerator * other.denominator) - (
            other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Multiply this fraction with the other fraction"""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Divide this fraction by the other fraction"""
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __floordiv__(self, other):
        """Integer divide this fraction by the other fraction"""
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        """Check if this fraction and the other fraction are equal"""
        num1 = self.__float__()
        num2 = other.__float__()
        return _fp_almost_equal(num1, num2)

    def __le__(self, other):
        """Check if this fraction is lesser than or equal to the other fraction"""
        num1 = self.__float__()
        num2 = other.__float__()
        return num1 <= num2

    def __lt__(self, other):
        """Check if this fraction is lesser than the other fraction"""
        num1 = self.__float__()
        num2 = other.__float__()
        return num1 < num2

    def __ge__(self, other):
        """Check if this fraction is greater than or equal to the other fraction"""
        num1 = self.__float__()
        num2 = other.__float__()
        return num1 >= num2

    def __gt__(self, other):
        """Check if this fraction is greater than the other fraction"""
        num1 = self.__float__()
        num2 = other.__float__()
        return num1 > num2

    def __float__(self):
        """Returns the decimal value of the fraction"""
        return self.numerator / self.denominator
