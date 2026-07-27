class Student:
    def __init__(self, name, marks):
        self.name = name          
        self.__marks = marks      

    # Setter method
    def set_marks(self, marks):
        self.__marks = marks

    # Getter method
    def get_marks(self):
        return self.__marks

# Create object
s = Student("Alice", 90)

# Access public attribute
print("Name:", s.name)

# Access private attribute using getter
print("Marks:", s.get_marks())

# Modify private attribute using setter
s.set_marks(95)

print("Updated Marks:", s.get_marks())
