import os

file_path = "/home/skc2277/Documents/Pyhton course/File-and-Error-handling/rough.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File is removed!")
else:
    print("File is not found")
