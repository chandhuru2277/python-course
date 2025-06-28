def loop(num):
    for x in range(num):
        yield x

temp= loop(5)
for n in temp:
    print(n)