# counting down?
for i in range(10, 0, -1):
    print(i)

print("*" * 10)
for i in range(2, 21, 2):
    print(i)

print("*" * 10)
for floor_number in range(1, 25):
    if floor_number == 13:
        continue
    print("Floor number", floor_number)