num="20"
# fill zero
print(num.zfill(5))
# right side 
print(num.rjust(5,'*'))
# left side 
print(num.ljust(5,'-'))
# center side
print(num.center(5,"="))

string= "    Hello world     "
# remove white space all side
print(string.strip())
# remove right side 
print(string.rstrip())
# remove left side
print(string.lstrip())
