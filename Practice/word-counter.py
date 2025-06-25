# get the user input
para= input("enter the message: \n")

# length of paragraph
print("length:", len(para))

# unique character count
unique_letter= {ch: para.count(ch) for ch in para if ch!=' '}
print("unique letter: ", len(unique_letter))

# word counter
length= len(para.split(" "))
print("word counter: ",length)