''' https://realpython.com/python-refactoring/#using-pycharm-for-refactoring

Objects That Should Be Functions

Sometimes there is object-oriented code which would be better suited to a simple function or two.
Some tell-tale signs of incorrect use of classes:
    Classes with 1 method (other than .__init__())
    Classes that contain only static methods

Take this example of an authentication class:
'''


class Authenticator(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        ...
        result = 'result of the authenticate method'
        return result


'''
It would make more sense to have a simple function named authenticate() that takes username and password as arguments:
'''


def authenticate(username, password):
    ...
    result = 'result of the authenticate function'
    return result
