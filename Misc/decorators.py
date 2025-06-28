import functools

# basic way
def my_decortors(myfun):
    def wrapper():
        print("Program start in wrapper")
        myfun()
        print("Program end in wrapper")
    return wrapper

def hello():
    print("Hello in hello function")

temp= my_decortors(hello)
temp()

# decorator way
def test(myfun):
    def wrapper(*args, **kwargs):
        print(f"Wrapper function  arg {args} kwargs{kwargs} ")
        print("sum: ",myfun(*args,**kwargs))
        print("Program end")
    return wrapper

@test
def add(x,y):
    return x+y

add(1,2)
