class Car:
    def move(self):
        print("Car is driving")

class Boat:
    def move(self):
        print("Boat is sailing")

class Plane:
    def move(self):
        print("Plane is flying")

vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    vehicle.move()
