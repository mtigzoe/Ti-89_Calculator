#import cmath as cm
from cmath import *
from modes.base_mode import BaseMode


class ComplexMode(BaseMode):   
    def calculateComplex(expression):
        return print(eval(expression))
