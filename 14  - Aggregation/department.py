# Assignment:
# Create a class Department and a class Employee. Use aggregation 
# by having a Department object store a reference to an Employee object that exists independently of it.


    
class Employee:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"Employee name: {self.name}")

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee
        
    def show_employee(self):
        print(f"Department: {self.name}")
        self.employee.display()

emp1 = Employee("Ayesha")
dep1 = Department("IT", emp1)
dep1.show_employee()
