from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class calculations: 
    history: List[Calculation] = [] #history is typeforced to be of type List, and each element will be of Calculation type