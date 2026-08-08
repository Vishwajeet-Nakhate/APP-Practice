# Python Generator Example

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i


# Creating a generator object
numbers = generate_numbers(5)

# Displaying generated values
print("Generated Numbers:")

for number in numbers:
    print(number)
