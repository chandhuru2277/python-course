res= {x:2**x for x in range(5)}
print(res)

word= "banana"
res= {x: word.count(x) for x in set(word)}
print(res)

# swap key and value
data= {'a':1, 'b':2}
res= {v:k for k,v in data.items()}
print(res)