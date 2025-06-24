status = True
while status:
    print("1.+")
    print("2.-")
    print("3.*")
    print("4./")
    print("5.//")
    print("6.%")
    print("7.**")
    print("8.exit")

    option = input("enter the option:\n")
    option = int(option)
    
    if option == 8:
        status = False
        print("exit")
    elif option == 1:
        a = int(input("enter 1'st number"))
        b = int(input("enter 2'nd number"))
        res = a+b
        print("sum: ", res)
    elif option == 2:
        a = int(input("enter 1'st number"))
        b = int(input("enter 2'nd number"))
        res = a-b
        print("sub: ", res)
    elif option == 3:
        a = int(input("enter 1'st number"))
        b = int(input("enter 2'nd number"))
        res = a*b
        print("mul: ", res)
    elif option == 4:
        a = int(input("enter 1'st number"))
        b = int(input("enter 2'nd number"))
        res = a/b
        print("div: ", res)
    elif option == 5:
        a = int(input("enter 1'st number"))
        b = int(input("enter 2'nd number"))
        res = a//b
        print("div(//): ", res)
    elif option == 6:
        a = int(input("enter 1'st number"))
        b = int(input("enter 2'nd number"))
        res = a%b
        print("mod: ", res)
    else:
        a = int(input("enter 1'st number"))
        b = int(input("enter 2'nd number"))
        res = a**b
        print("expo: ", res)
