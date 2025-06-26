import random

lc_alpha = list("abcedfghijklmnopqrstuvwz")
uc_alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbol = list("!@#$%^&*?~")

password=[]
str_password=""

for x in range(4):
    num = str(random.randint(0, 9))
    password.append(num)
    password.append(random.choice(lc_alpha))
    password.append(random.choice(uc_alpha))
    password.append(random.choice(symbol))

for ch in password:
    str_password+=ch
print(str_password)

