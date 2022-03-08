import cmath as cm

from modes.base_mode import BaseMode


class ComplexMode(BaseMode):   
    def calculate(self, expression):
        return eval(f"cm.{expression}")
