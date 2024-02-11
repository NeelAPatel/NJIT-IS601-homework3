from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


# Main calculator class
class Calculator:

    # @staticmethod = GLOBALLY accessible, does NOT have access to outside values/instance varibales
    # -- strict job is to take input vars => redirect. little to no calculation
    # -- Also may return result. AKA just an action method
    # Method = attached inside a class

    # Instance of Calculation-class is created, storing a,b,operation
    # THEN actual calculation is performed while returning
    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add)  
        return calculation.get_result()
    
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)  
        return calculation.get_result()
    
    @staticmethod
    def multiply (a,b):
        calculation = Calculation(a, b, multiply)  
        return calculation.get_result()
    
    @staticmethod
    def divide(a,b):
        # Why not just do this? 
        return Calculation(a, b, divide).get_result()
