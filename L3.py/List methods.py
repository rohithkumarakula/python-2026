#List methods in python

#--------------------------- list.append()--------------
# we can add elements to list

list = [1, 2, 3]
list.append(4) 
print(list)

#--------------------------list.sort()---------------
#sorts in ascending order

list = [6, 2, 3]
list.append(9) # we can also add num
list.sort() 
print(list)


#--------------------------list.sort(reverese = True)---------
#sorts in descending order
list = [2, 7, 4, 9, 87, 99, 1919]
list.sort(reverse=True)
print(list)

list = ["apple", "banana", "litchis"]
list.sort(reverse=True)
print(list)


#---------------------------list.reverse()--------------
#reveres the list

list = [22, 33, 44, 55, 66, 11]
list.reverse()
print(list)

#-------------------------list.insert(idx,el)---------------
#insert element at index

list = [2,1,3,]
list.insert(1,5)  # 5 will goes to 1st index place, the rest follows
print(list)

#-----------------------list.remove(1)-------------------
#removes first occurenece of element 

list = [2,1,3,1]
list.remove(1)  # here first 1 at index 1 was removed
print(list)

#----------------------list.pop(index)----------------
# removes element at indes=x

list = [2, 1, 3, 1]
list.pop(2)  # here 2 is index value, so 3 in list will be removed
print(list)