#wap to ask user to enter names of their 3 favorite movies and store them in a list
movies = []
movie1 = input("enter 1st fav movie: ")
movie2 = input("enter 2nd fav movie: ")
movie3 = input("enter 3rd fav movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)


#wap to check if a list contains a palindrome of elements .

list1 = [1,2,1]


copylist1 = list1.copy()
copylist1.reverse()

if (copylist1 == list1):
    print("palindrome")
else:
    print("not palindrome")

""" 1. create a list
    2. create a duplicate list name, copylist1
    3. reverse the copylist1 which is duplicate
    4. then we check dup and rev are same or not 
"""

name = ['racecar']

dupname = name.copy()
dupname.reverse()

if (name == dupname):
    print("palindrome")
else:
    print("not palindrome")


# wap to count the number of students with the 'A' grade in the following tuple
# ["C", "D", "A", "A", "B", "B", "A"]
# store the above values in a list & sort them "A" to "D"

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)