# Assignment:
# Create a class Engine and a class Car. 
# Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Car *has* an Engine

    def start_car(self):
        self.engine.start()   # Use the Engine's start method

# Create an Engine object
engine1 = Engine()

# Pass Engine object to Car
my_car = Car(engine1)

# Start the car (which starts the engine)
my_car.start_car()

