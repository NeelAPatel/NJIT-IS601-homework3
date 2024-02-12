# Class is created and used to specifically execute a calculation 

from decimal import Decimal # Importing Decimal to typeforce 
from typing import Callable # Allows hinting to operation variable that its a callable function
class Calculation: 
    # Callable [input params types, output param type]; since you need two inputs, its [decimal,decimal]
    def __init__ (self,a: Decimal,b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
         # Instance variables
        self.a = a
        self.b = b
        self.operation = operation # This allows any operation function to be triggered by calculation

    def get_result(self): 
        # Calls the stored operation function AS operation() and uses a,b on it
        # -- basically renames operations into a singular function since 
        # -- all 4 use same number and type of parameters
        return self.operation(self.a, self.b)