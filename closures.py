def outer():
    message = "Hello"

    def inner():
        print(message)   

    return inner

greet = outer()
greet()
