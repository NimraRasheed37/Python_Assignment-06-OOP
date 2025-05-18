# Assignment:
# Create a class decorator add_greeting 
# that modifies a class to add a greet() method 
# returning "Hello from Decorator!". Apply it to a class Person.

# function pre defined to use in class
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls
    
    
# class decorator will pass on pre defined function to class
@add_greeting
class Person:
    pass

person = Person()
print(person.greet())
    