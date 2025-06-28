my_list= [1,2,3,4,5]
myfrist_iter= iter(my_list)

print(myfrist_iter.__next__())
print(myfrist_iter.__next__())
print(myfrist_iter.__next__())
print(myfrist_iter.__next__())
print(myfrist_iter.__next__())

mysecond_iter= iter(my_list)

for num in mysecond_iter:
    print(num)

mythird_iter= iter(my_list)

while True:
    try:
        value= next(mythird_iter)
        print(value)
    except StopIteration:
        break