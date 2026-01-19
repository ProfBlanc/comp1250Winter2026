are_lights_on_str = "yes"
# you can convert between data types
are_lights_on_bool = bool(are_lights_on_str)
# when converting to boolean (bool()) if value is NOT empty or zero => True.
# else => Flase
print(are_lights_on_bool)
print("*" * 10)

age = "50"  # is age a str or int or float?
print(type(age))
age = int(age)
print(type(age))
age = int(age)
age = "50"
age = float(age)
print(type(age))

# you can convert str to int, float, boolean => no issues
# you can convert ANY data to to str() => no issues
temperature = 10.5
temperature = int(temperature)
print(temperature)
temperature = float(temperature) + 0.5
print(temperature)

# if you attempt to convert a non-numerical str to int or float

size = 0xf  # zero + x letter => hex num => base 16
print(size)
size = 0b1010
print(size)
size = 0o17  # zero + o letter => octal => base 8
print(size)




