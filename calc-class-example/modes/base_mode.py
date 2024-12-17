import sympy as sym
import statistics
import re


class BaseMode:
    def __init__(self):
        self.test = 0

    # Every class that inherits from this one will be able to meow.
    def meow(self):
        print("Meow!!")
