class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Nimra", 90)
s2 = Student("Alia", 85)

s1.display()
s2.display()