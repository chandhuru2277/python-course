range = 10
system_guessing_num = 6
life = system_guessing_num / 2

while life > 0:

    user_guessing_num = int(input("Enter the guess number: "))
    if user_guessing_num == system_guessing_num:
        print("Super your guess correct :) that number is ", user_guessing_num)
        exit()
    elif user_guessing_num > system_guessing_num:
        print("your number so long!")
        life -= 1
    else:
        print("your number is so short!")
        life -= 1
print("your are lost!")
