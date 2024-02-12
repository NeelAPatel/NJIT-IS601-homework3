from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations: 
    #Stores all 'Calculation's performed
    #history is typeforced to be of type List, and each element will be of Calculation type
    history: List[Calculation] = [] 


    # @Classmethod = affects ALL instances. any instance can add to the one singular history variable
    # cls keyword means itself but class type. affects all classes. 
    # self keyword therefore works for instances only
    @classmethod
    def add_to_history(cls, calculation: Calculation): 
        cls.history.append(calculation)
    
    @classmethod
    def clear_history(cls): 
        cls.history.clear() #empties the list


    # Returns latest Calculation element
    # -1 index = last index by looping backwards
    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.history: #If history exists
            return cls.history[-1]
        return None
    
    #     @classmethod
    # def find_by_operation(cls, operation_name: str) -> List[Calculation]:
    #     """Find and return a list of calculations by operation name."""
    #     return [calc for calc in cls.history if calc.operation.__name__ == operation_name]