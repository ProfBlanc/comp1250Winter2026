
def order_tshirt(shirt_size:int, shirt_type:str, shirt_color:list[str])->str:
    is_valid = True
    if isinstance(shirt_size, int) and shirt_size in [1,2,3]:
        print("Good values entered for size_size")
    else:
        is_valid = False

    if isinstance(shirt_type, str) and shirt_type in "short,long,sweater".split(","):
        print("Good values entered for shirt_type")
    else:
        is_valid = False

    if isinstance(shirt_color, list) and len(shirt_color) > 0:
        for v in shirt_color:
            if not isinstance(v, str):
                print("Invalid value for shirt_color. Not all values are strings")
                is_valid = False
        print("Validation for shirt_color finished.")

    return "Good job!" if is_valid else "Bad job!"

"""
def order_tshirt(shirt_size, shirt_type, shirt_color):
    pass
"""
result1 = order_tshirt(1, "short", ["red", "white"])
print("*" * 10)
result2 = order_tshirt("blah", 1234, True)

print(result1, result2, sep='\n')
