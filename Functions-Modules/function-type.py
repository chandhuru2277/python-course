# no return no argument
def greet():
    print("Hello world")

# no return with argument
def add(a, b):
    print("sum: ", a + b)

# with return no argument
def sub():
    return 20 - 10

# with return with argument
def mul(a, b):
    return a * b

greet()
add(10, 20)
print(sub())
print(mul(10, 20))
