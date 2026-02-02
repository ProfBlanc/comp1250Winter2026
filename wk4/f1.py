"""
list = collection of values

"""
name = "John"
age = 100
temp = -10.5

values = ["Mary", 50, -25.5, True, 1, "One"]
#          0       1     2    3    4    5
#          -6     -5   -4  -3    -2    -1

print(len(values))  # 3
print(values[-3])  # third last value
print(values[len(values) - 3])  # len(values) - 3

# list slicing => pizza pie
# retrieve a sublist of a list. certain values of list
first_two = values[0:2]  # n1 = start index, n2 = end index exclusive
print(first_two)
first_two_neg = values[-6:-4]
print(first_two_neg)

every_other_value = values[0:len(values):2]  # 0 : 6 : 2
# start, end, skip=how to change index count
print(every_other_value)
every_even_value = values[1::2]
# what happened to second number? using default value
valid = values[::]
# n1 have default of 0,
# n2 has default of len(list),
# n3 has default of 1
print(every_even_value)
print(valid)

print(values[-3:])
print(values[::-1])
