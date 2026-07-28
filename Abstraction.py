from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child class
class Dog(Animal):
    def sound(self):
        return "Bark"

# Child class
class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating objects
dog = Dog()
cat = Cat()

print("Dog:", dog.sound())
print("Cat:", cat.sound())
