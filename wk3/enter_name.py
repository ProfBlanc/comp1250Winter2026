name = input("Enter you first and last name separated by a space: ")

if " " in name:
    print("Great!")
else:
    print("Not great!")

print("Great" if " " in name else "Not great")

# bool_expression ? statement to execute if true : statement to execute if false