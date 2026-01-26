age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
if age < 5:
    print("You are an enfant")
if age < 13:
    print("You are a child")
if age < 18:
    print("You are a teenager")
else:
    print("You are an adult")