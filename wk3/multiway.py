age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("You are an enfant")
elif age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
else:
    print("You are an adult")