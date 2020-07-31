"""
Calculator class containing basic math operations.
"""


class Calculator(object):
    def __init__(self, first_term, second_term):
        self.first_term = first_term
        self.second_term = second_term

    def add(self):
        return self.first_term + self.second_term

    def subtract(self):
        return self.first_term - self.second_term

    def multiply(self):
        return self.first_term * self.second_term

    def divide(self):
        if self.second_term == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.first_term / self.second_term

    # Write a method to calculate the square of a term (Python ** operator is used to calculate the power of a number)

    # Write a method to calculate the square root of a term
