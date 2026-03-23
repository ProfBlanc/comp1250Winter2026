filename = "t1.txt"
# mode = "a"
mode = "r+"

# for each mode, you can add a plus sign
# r+, w+, a+
# + => also support opposite operation

fo = open(filename, mode)
fo.seek(11)
content = fo.read(8)
fo.write("Move other! ")
fo.close()
print(content)