# check the element
set_1 = {1, 2, 3, 4}
set_2 = {1, 5, 6,2}
print(6 in set_2)

# subset
print({1,2}.issubset({1,2,4,5}))

# superset
print({1,2,3,4}.issuperset({1,3}))

# disjoint
print({1,2,3,4}.isdisjoint({5,6}))