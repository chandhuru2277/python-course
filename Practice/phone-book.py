contacts = dict()

status = True

while status:
    print("1.add")
    print("2.view")
    print("3.exit")

    option = int(input("Choose the option"))

    if option == 1:
        name = input("Enter the name:")
        mobile = int(input("Enter the mobile number:"))
        contacts.update({name: mobile})
    elif option == 2:
        print(contacts)
    else:
        status = False
