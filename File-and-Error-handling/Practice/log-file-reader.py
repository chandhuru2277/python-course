def show():
    with open("File-and-Error-handling/Practice/log/app.log", "r") as file:
        for line in file:
            print(line.strip())

def find(text):
    with open("File-and-Error-handling/Practice/log/app.log", "r") as file:
        for line in file:
            if text in line:
                print(line)

status = True

while status:
    print("1.view")
    print("2.find")
    print("3.exit")
    choice = int(input("enter the choice: "))

    if choice == 1:
        show()
    elif choice == 2:
        search_text = input("enter the log level(ERROR,INFO,WARNING): ").upper()
        find(search_text)
    elif choice == 3:
        status = False
    else:
        status = False
