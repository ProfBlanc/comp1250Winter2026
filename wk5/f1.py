"""

loop
    iteration structure
        a block/chunk of code that will be repeated

for
    use when you want to repeat action for a known amount of times

while
    use when you want to repeat action based on a condition
"""

name = input("Enter your name: ")

for letter in name:
    print(letter)

values = [123, 45.67, True, "hello"]

for value in values:
    print(value)

for i in range(5):
    print(i)
