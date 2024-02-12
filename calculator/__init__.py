from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal # Importing Decimal to typeforce 


# Main calculator class
class Calculator:


    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        # create instance of a single calculation
        myCalculation = Calculation.create(a,b, operation)

        #using Calculation class itself bc we are doing it for the entire class
        Calculations.add_to_history(myCalculation)
        return myCalculation.perform()


    # @staticmethod = GLOBALLY accessible, does NOT have access to outside values/instance varibales
    # -- strict job is to take input vars => redirect. little to no calculation
    # -- Also may return result. AKA just an action method
    # Method = attached inside a class

    # Instance of Calculation-class is created, storing a,b,operation
    # THEN actual calculation is performed while returning
    @staticmethod
    def add(a: Decimal, b: Decimal):
        calculation = Calculation(a, b, add)  
        return calculation.get_result()
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal):
        calculation = Calculation(a, b, subtract)  
        return calculation.get_result()
    
    @staticmethod
    def multiply (a: Decimal, b: Decimal):
        calculation = Calculation(a, b, multiply)  
        return calculation.get_result()
    
    @staticmethod
    def divide(a: Decimal, b: Decimal):
        # Why not just do this? 
        return Calculation(a, b, divide).get_result()
