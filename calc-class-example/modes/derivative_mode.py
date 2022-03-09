import sympy as sym

#from modes.base_mode import BaseMode


class DerivMode:
    def __init__(self):
        self.x2, self.y2 = sym.symbols("x y")
        # m = x**4+x*y**4
        self.intex = sym.symbols("x")
    def calculate(self, expression):
        return eval(f"sym.{expression}")
