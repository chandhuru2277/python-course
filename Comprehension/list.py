l1= [1,2,3,4,5,6]

# without condition
res= [ x**2 for x in l1]
print(res)

# with condition
res= [x**2 for x in l1 if x%2==0]
print(res)

# nested loop
res = [(x,y) for x in [1,2] for y in [3,4]]
print(res)

# flatten 2D
matrix= [ [1,2,3], [4,5,6]]
res= [ num for row in matrix for num in row]
print(res)