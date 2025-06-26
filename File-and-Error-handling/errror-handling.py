try:
    num=int(input("Enter the number"))
    result= 10/num
except ValueError:
    print("please enter the value")
except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print(result)
finally:
    print("always run")
    