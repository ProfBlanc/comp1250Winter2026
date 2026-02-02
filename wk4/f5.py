values = list(range(1, 6)) + list(input("Enter a value: "))
print(values)
# a list method is an action on a list
# .method_name([arguments])
values.append(50)  # add a value. only add 1 value at a time
# add at the end hence append
#values.append(1, 2)
values[0] = "11"
values.remove(3)  # warning: you need to ensure value
# exists before removing
print(values)

search = 4
if search in values:
    print("index of", search, "is", values.index(search))

if search in values:
    values.remove(search)

values.pop(-1)

#values.sort()  # data type are all the same else, comparison
values.count("b")

values.extend( list("abc")  )
print(values)