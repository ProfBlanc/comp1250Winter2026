print("Hello" + " " + "World")  # notice the plus sign
# notice that we do not use a comma in print statement
# using plus sign = concatenation = merging values
# when using concatenation, data types must be compatible
# str-str, int-int, float-int, float-to-float,
# bool-int, bool-float
#print('I am ' + 100 + " years old")
print('I am' , 100 , "years old")
print('I am ' + str(100) + " years old")
print("*" * 20)
# 4 fundamental data types
# string => str()
# integer => int()
# float => float()
# boolean => bool() => True or False => alias (shortcut) to values 0 and 1

#alphnumerical. first letter is underscore or letter
# second char and onwards is alphanumerical + underscore

temperature = -10
weight = 50.5
name = "John Doe"
age = 45
is_learning_python = True
thisIsAnExampleOfCamelCase = False

print("My name is " + name + "!")
print("I am " + str(age) + " years old")
print("It is", temperature, "degrees Celsius outside today")
print("Are you learning python?", is_learning_python, sep="\t" * 2)
