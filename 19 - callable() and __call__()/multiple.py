# Assignment:
# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor
    
multiply_by_5 = Multiplier(5)

# Test 1
print("Is multiply_by_5 callable?", callable(multiply_by_5))

# Test 2
result = multiply_by_5(10)
print("10 multiplied by 5 is:", result) 

# Test 3
multiply_by_3 = Multiplier(3)
print("7 multiplied by 3 is:", multiply_by_3(7)) 