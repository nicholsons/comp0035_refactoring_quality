# This example is from RealPython available here: https://realpython.com/python-refactoring/#using-pycharm-for-refactoring


class Line(object):
    def __init__(self, name_en: str, name_jp: str, color: str, number: int, sign: str):
        self.name_en = name_en
        self.name_jp = name_jp
        self.color = color
        self.number = number
        self.sign = sign

    def __repr__(self):
        return f"<Line {self.name_en} color='{self.color}' number={self.number} sign='{self.sign}'>"

    def __str__(self):
        return f"The {self.name_en} line"


'''Refactored version using dataclass (works for Python 3.6 and later)'''
from dataclasses import dataclass


@dataclass
class Line(object):
    name_en: str
    name_jp: str
    color: str
    number: int
    sign: str


'''Refactored version using attribs (works for Python 3 - 3.5). You need to install the package attr'''
from attr import attrs, attrib


@attrs
class Line(object):
    name_en = attrib()
    name_jp = attrib()
    color = attrib()
    number = attrib()
    sign = attrib()
