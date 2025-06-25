a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

res={}
for x in a:
    if x in res:
        res[x]+=1
    else:
        res[x]=1
print(res)

# using comprehension
result={ item: a.count(item) for item in set(a)}
print(result)