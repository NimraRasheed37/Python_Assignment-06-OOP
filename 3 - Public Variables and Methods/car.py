class Car:
    def __init__(self, brand):
        self.brand = brand
        

    def start(self):
        print(f"My {self.brand} car is starting")

c1 = Car("Volvo")
c2 = Car("BMW")

c1.start()
c2.start()
