import json

data= {
    'name': "william",
    'age':10
}

with open("File-and-Error-handling/temp.json","w") as f:
    json.dump(data,f)

with open("File-and-Error-handling/temp.json","r") as f:
    res= json.load(f)
    print(res)
