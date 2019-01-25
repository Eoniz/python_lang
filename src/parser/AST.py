from equality import *

class Aexp(equality.Equality):
    pass

class IntAexp(Aexp):
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return f'IntAexp(i="{self.i}")'

