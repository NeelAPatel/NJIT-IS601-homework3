
# Class is created and used to specifically execute a calculation 
class Calculation: 
    def __init__ (self,a,b, operation):
         # Instance variables
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self): 
        # Calls the stored operation function AS operation() and uses a,b on it
        # -- basically renames operations into a singular function since 
        # -- all 4 use same number and type of parameters
        return self.operation(self.a, self.b)