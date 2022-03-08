import math as m

from modes.base_mode import BaseMode


class RealMode(BaseMode):
    def __init__(self):
        #self.expression = expression     
        pass 
    def calculate(self, expression):
        return eval(f"m.{expression}")

