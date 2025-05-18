# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# # Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Showing from class A")
    
class B(A):
    def show(self):
        print("Showing from class B")

class C(A):
    def show(self):
        print("Showing from class C")

class D(B, C):
    
    # if we pass d.show will print message from B first, and if donest have any message, it will print C first
    pass
    # if we print message in D, it will show first
    # def show(self):
    #     print("Showing from class D")

d = D()

d.show()

print(D.mro())