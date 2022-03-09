from modes.derivative_mode import DerivMode
from modes.complex_mode import ComplexMode
from modes.real_mode import RealMode
from modes.statistics_mode import StatsMode

import sympy as sym
import statistics
import re


class BaseMode(ComplexMode,DerivMode, \
    RealMode, StatsMode):
    def __init__(self):
        self.test = 0
        super()

    # Every class that inherits from this one will be able to meow.
    def meow(self):
        print("Meow!!")
