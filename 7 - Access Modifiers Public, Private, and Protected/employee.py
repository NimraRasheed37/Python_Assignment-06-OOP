# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
    
    
    def show_info(self):
        print(f"\nName: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
    
emp1 = Employee("John Doe", 50000, "123-45-6789")
# Accessing public variable
print(emp1.name)      # this works fine
print(emp1._salary)   # this works fine too

# print(emp1.__ssn)  -> This gives an error because __ssn is private
# 
print(emp1._Employee__ssn) # we can access private data using name mangling

# or we can use show_info() method that is define inside class
emp1.show_info()

