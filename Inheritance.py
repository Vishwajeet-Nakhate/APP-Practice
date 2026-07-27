# Parent Class
class Animal:
    def sound(self):
        print("Animals make sounds.")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog barks.")

# Create object of Child Class
d = Dog()

# Access parent class method
d.sound()

# Access child class method
d.bark()
