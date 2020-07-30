'''
Example from: https://realpython.com/python-refactoring/#using-pycharm-for-refactoring

Converting “Triangular” Code to Flat Code

These are the symptoms of highly nested code:
    A high cyclomatic complexity because of the number of code branches
    A low Maintainability Index because of the high cyclomatic complexity relative to the number of lines of code

Take this example that looks at the argument data for strings that match the word error. It first checks if the data
argument is a list. Then, it iterates over each and checks if the item is a string. If it is a string and the value is
"error", then it returns True. Otherwise, it returns False:
'''


def contains_errors(data):
    if isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                if item == "error":
                    return True
    return False


''' 
Refactored version 

We can refactor this function by “returning early” to remove a level of nesting and returning False if the 
value of data is not list. Then using .count() on the list object to count for instances of "error". The return value 
is then an evaluation that the .count() is greater than zero:
'''


def contains_errors(data):
    if not isinstance(data, list):
        return False
    return data.count("error") > 0
