d1 = {"name": "william", "id": 2277, "martial_status": False}
print(d1)
# update the element
d1.update({"name": "sekar"}) 
print(d1)
 # add element
d1.update({"college": "TMC", "code":322, "pincode": 622222})
print(d1)
# pop specific keys
print(d1)
d1.pop("college") 
# pop item (remove last element)
d1.popitem()
print(d1)
# delete entry
d1.update({"device": "mobile", "model": 2978,"price": 3434})
print(d1)
del d1["model"]
print(d1)
# clear
d1.clear()
print(d1)