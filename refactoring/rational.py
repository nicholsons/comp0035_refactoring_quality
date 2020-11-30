# From https://www.jetbrains.com/help/pycharm/product-refactoring-tutorial.html#4fb31
# The instructions are contained in the link above.
from collections import namedtuple


class Rational(namedtuple('Rational', ['num', 'denom'])):

    def __new__(cls, num, denom):
        if denom == 0:
            raise ValueError('Denominator cannot be null')
        if denom < 0:
            num, denom = -num, -denom
        return super().__new__(cls, num, denom)

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)