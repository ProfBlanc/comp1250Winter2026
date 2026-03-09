"""
series of values
    list: most dynamic. mutable. index tracker. any data type
    tuple: less dynamic than list. why? immutable. index tracker. any data type
    set: restrictive. unique values. cannot include individual mutable values. no index tracker



"""

s1= { (1,2), "hi", False, "hello" }

"""
a dictionary is a book that contains definitions of words
to get a definition, we must look up a word

word = key to finding the definition
definition = value

a data-type that stores key-value pairs

"""

d1 = dict()
d2 = {}  #
print(type(d2))

d1["firstname"] = "Ben"
d1["lastname"] = "Blanc"

d3 = {
    "age": 100,
    "weight": 45.6,
    "name": "John",
    0: "zero",
    1: "one",
    2: "two",
    1.1: "num",
    }
print(d3)