from abc import ABC, abstractmethod

# Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


# Factory Class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animal_type = animal_type.lower()

        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        elif animal_type == "cow":
            return Cow()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


# Client Code
if __name__ == "__main__":
    animal = AnimalFactory.create_animal("dog")
    print(animal.speak())  # Woof!

    animal = AnimalFactory.create_animal("cat")
    print(animal.speak())  # Meow!

    animal = AnimalFactory.create_animal("cow")
    print(animal.speak())  # Moo!
