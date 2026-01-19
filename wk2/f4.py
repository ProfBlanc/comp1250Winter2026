# getting user input
# input() => prompt the user
name = input("Enter your name: ")
print("Hello, " + name)
print("Hello,", name)
print(type(name))
age = input("Enter age: ")
age = int(age)
print(name, "is", age, "years old", sep='\t', end='!' * 5 + "\n")  # '!!!!!\n'
print(" Next sentance")


