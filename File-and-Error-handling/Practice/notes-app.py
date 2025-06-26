import os


def file_create(filename, content):
    working_path = "File-and-Error-handling/Practice/diary/"
    file_path = working_path + filename
    action = "w"
    with open(file_path, action) as f:
        f.write(content)
        print("******************************************")
        print(filename, " file is created")
        print("******************************************")


def file_append(filename, content):
    working_path = "File-and-Error-handling/Practice/diary/"
    file_path = working_path + filename
    action = "a+"
    with open(file_path, action) as f:
        f.write(content)
        print("******************************************")
        print(filename, " file is updated")
        print("******************************************")


def file_show():
    path = "File-and-Error-handling/Practice/diary"
    entries = os.listdir(path)
    print("******************************************")
    for file in entries:
        print(file)
    print("******************************************")


def file_view(filename):
    working_path = "File-and-Error-handling/Practice/diary/"
    file_path = working_path + filename
    action = "r"
    with open(file_path, action) as f:
        print(f.read())


def file_delete(filename):
    working_path = "File-and-Error-handling/Practice/diary/"
    file_path = working_path + filename

    if os.path.exists(file_path):
        os.remove(file_path)
        print(file_path, " path file is deleted")
    else:
        print(file_path, " path file is not found!")

status = True

while status:
    print("---------------------------------------------")
    print("1.file create")
    print("2.file update")
    print("3.file list")
    print("4.file view")
    print("5.file delete")
    print("6.exit")
    print("---------------------------------------------")

    choice = int(input(("enter the choice: ")))

    if choice == 1:
        print("===========================================")
        filename = input("enter the file name with type: ")
        content = input("enter the content: ")
        file_create(filename, content)
        print("===========================================")

    if choice == 2:
        print("===========================================")
        filename = input("enter the file name with type: ")
        content = input("enter the content: ")
        file_append(filename, content)
        print("===========================================")

    if choice == 3:
        file_show()

    if choice == 4:
        print("===========================================")
        filename = input("enter the file name with type: ")
        file_view(filename)
        print("===========================================")

    if choice == 5:
        print("===========================================")
        filename = input("enter the file name with type: ")
        file_delete(filename)
        print("===========================================")

    elif choice == 6:
        status = False
