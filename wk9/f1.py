"""
What is a function:
    a name that points to a series of steps to execute
        produces a mini script

Why functions?
    DRY
        Don't Repeat Yourself

        easier to maintain when code is not repeated

to create function, use def keyword, name of function, perenthesis

it is like placing an order

in a function, you can create placeholders/variables that
modify how the function behaves/what the function produces
    parameters

"""

def name_of_function():
    pass  # empty body

def order_tshirt(shirt_size, shirt_type, shirt_color):
    # print(shirt_size, shirt_type, shirt_color)

    return "Ordered was processed with values " + shirt_size + "," + shirt_type + "," + shirt_color


"""
scope = accessibility of a variable
    two scopes
        global: var declared outside of a function or for loop
        local: var declared inside a function or for loop
"""

result1 = order_tshirt("medium", "long-sleeved", "blue")

result2 = order_tshirt("large", "short-sleeved", "orange")

size = "small"
s_type = "sweater"
s_color = "beige"

result3 = order_tshirt(size, s_type, s_color)

print(result1, result2, result3, sep='\n')

user_shirt_size = input("Enter a shirt size")
user_shirt_type = input("Enter a shirt type")
user_shirt_color = input("Enter a shirt color")

order_tshirt(shirt_color=user_shirt_color, shirt_size=user_shirt_size, shirt_type=user_shirt_type)

# using named parameter execution

print("value1", "value2", sep='\t', end='!\n')
