# *args (tuple - no keyword argument)
# **kwargs (dictionary - keyword argument)

def add(*args):
    print(args)
add(1,2,3,4)

def table(**kwargs):
    print(kwargs)
table(a=10,b=20)

def matrix(*args, **kwargs):
    print(args)
    print(kwargs)
matrix(11,22,a=33,b=44)