"""

Reading files

open(file, mode)

operations
    read()      returns entire file contents
    readline()  return file contents up until it encounters \n
    readlines() returns list of entire contents
                each index represents a sentence in list
                a sentence = when file encounters a \n char

"""

filename = "t1.txt"
mode = "r"

fo = open(filename, mode)  # runtime error or not?

# example 1
#contents = fo.read()
# example 2
# contents = fo.read(11)  # read([number_of_bytes])
# example 3
# contents = fo.readline()
# contents += fo.readline()

# example 4
contents = fo.readlines()

fo.close()

print(contents)


