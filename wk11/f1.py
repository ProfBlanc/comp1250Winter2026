"""
File Manipulation
    persistent data
        1) database
        2) file CRUD operations


2 components
    1) file name and/or location
        by default, location = cwd (current working directory)
        filename = name + extension
    2) file operation mode
        R       read
        A       append      add content to end of file
        W       write       remove content + add new content to file

Read: file needs to already exist
A & W: file is created if it does not exist

open()      global method for file manipulation
open()      returns a file object


writing:
    write(str_values)
    writelines(collection_value)
"""

# fo = open("t1.txt", "w")
fo = open("t1.txt", "a")
#fo.write("Hello World\n")

lines = "I love python,this is another line,final line here".split(",")
# lines = ["I love python", "this is another line", "final line here"]
print(lines)
# list comprehension
# syntax that combines for loop & list creation
#lines = [line + "\n" for line in lines]
lines = [sentence + "\n" for sentence in lines if "line" not in sentence]

fo.writelines(lines)
fo.close()

