# tuple is list a list
# series of values
# immutable => cannot be changed once set

a = (1, 2, "a", "b", True)
print(a)

b = tuple(range(1,6))
c = tuple("hello world")
d = a + b + c
e = d * 3
print(b, c, d, e, sep = "\n")

print(1 in b)

if 2 in a:
    print("Index of", 2, "is", a.index(2))

f = d[0: 10: 3]
print(f)