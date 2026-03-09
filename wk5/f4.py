"""
loop has 3 components
    starting condition/value
    advance from starting to ending condition/value
    ending condition/value
"""
start = 1
end = 10
update = 2

while start <= end:

    print(start)

    start += update
print("*" * 10)
# continually ask until a condition is meet
# continually ask user for an even number
num = 1
tries = 0
while num % 2 == 1 and tries < 5:
    tries += 1
    num = int(input("Enter an even number: "))
    if num % 2 == 0:
        print("Congrats! You entered an even number")
    else:
        print("Sorry, you entered an odd number")