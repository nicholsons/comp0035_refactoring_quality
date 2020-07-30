# From Martin Fowler refactoring
from dataclasses import dataclass


@dataclass
class Invoice(object):
    customer: str


def calculate_outstanding():
    pass


def print_owing(invoice):
    outstanding = calculate_outstanding()

    # Print details
    print('name: {0}'.format(invoice.customer))
    print('amount: {0}'.format(outstanding))


''' Refactored version
In PyCharm:
Select lines 18 and 19 and press CTRL+T
Select Refactor > Extract Method
Change the method name to print_details and 
'''


def print_owing_refactored(invoice):
    outstanding = calculate_outstanding()
    print_details(invoice, outstanding)


def print_details(invoice, outstanding):
    print('name: {0}'.format(invoice.customer))
    print('amount: {0}'.format(outstanding))
