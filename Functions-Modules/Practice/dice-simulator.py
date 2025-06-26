import random

status= True
while status:
    print("----------------------")
    print("1.Roll the dice")
    print("2.Exit")
    print("----------------------")
    choice= int(input("Enter the choice: \n"))

    if choice==1:
        print("=============================")
        print("your dice number:",end=" ")
        print(random.randint(1,6))
        print("=============================")
    else:
        status=False






