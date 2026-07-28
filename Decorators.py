def decorator(func):
    def wrapper(name):
        print("Welcome!")
        func(name)
        print("Thank you!")
    return wrapper

@decorator
def greet(name):
    print("Hello,", name)

greet("Alice")
