#strings is data type that stores a sequence of characters.
'''
str1 = "this is a string1"
str2 = 'string2'
str3 = """string2"""
'''


#escape sequence characters
str = "This is a string.\nwe are creating it in pyton" #\n means new line
print(str)

str1 = "This is a string.\twe are creating it in pyton"  #\t means tab space
print(str1)


#concatenation

str1 = "rohith"
str2 = "kumar"
final_str = str1+str2
print(final_str)

#length of str
print(len(str1))
print(len(str2))


#indexing - starts from 0

str = "rohith kumar"
print(str[0])
print(str[-7])

#slicing - Accessing parts of a string

str = "Rohith kumar"  # starts from 0 index 
print(str[0:])
print(str[0:4])

#slicing - Negative index 
#APPLE= e value -1, a value -5

str = "apple"
print(str[-3:-1])  #pl
print(str[-5:-2])  #app


#---------------------------string functions ----------------------

#1)------------------------------------str.endswith - returns true if string ends with substr-------------------------------

str = "I am studying python"
print(str.endswith('thon')) 

#2) str.capitalize() - capitalizes 1st char
str = "i am studying python"
print(str.capitalize()) # output = I
print(str) # this will print "i am studying python"

#3) str.replace(old, new)
str = "I am studying python"
print(str.replace("python", "java"))
print(str.replace("n", "m"))


# 4) str.find(word)

str = "I am studying python from Apna college"
print(str.find('y'))
print(str.find('I'))
print(str.find('i'))
print(str.find('from'))
print(str.find('q')) #there is no q in str so it returns -1


# 5) str.count("am")
str = "I am studying python from Apna college"
print(str.count("y"))

