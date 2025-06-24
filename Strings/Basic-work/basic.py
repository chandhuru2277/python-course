# create a string
movie_name = "wolverine"
# print the string
print(movie_name)
# access the character by positive order
ch= movie_name[2]
print(ch)
# access the character by negative order
ch= movie_name[-2]
print(ch)
# slicing string start from 2 end 5
print(movie_name[2:5])
# slicing string start from 0 end 5
print(movie_name[:5])
# slicing string start from 5 end size of string
print(movie_name[5:])
# slicing string start from 0 end with size of string
print(movie_name[::])
# slicing string start from -1 end with size of string negative order like (reverse)
print(movie_name[::-1])
# delete the string 
del movie_name
#print(movie_name)  error: because movie name not defined

# multi line string
movie_name= """This is the first paragraph
now i print this"""
print(movie_name)