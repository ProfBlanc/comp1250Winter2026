"""
f1-f3:
    operations for files

this module, operations for file system
    Explorer
    Finder
"""
import os   # operating system

print(os.name)  # nt for windows
print(os.pathsep)  # ;
print(os.sep)   # path seperator, \ for windows1

if not os.path.exists("my_dir1"):
    os.mkdir("my_dir1")

new_path = os.path.join("my_dir1", "my_dir2", "my_dir3", "my_dir4")
# create a proper path using the text passed in join statement
# my_dir1\my_dir2

# os.mkdir(new_path)
os.makedirs(new_path)