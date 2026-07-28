# Child class
class Engine:
    def start(self):
        print("Engine started")

# Parent class
class Car:
    def __init__(self):
        self.engine = Engine()   # Composition

    def drive(self):
        self.engine.start()
        print("Car is moving")

# Create object
car = Car()
car.drive()
