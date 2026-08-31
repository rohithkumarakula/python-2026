#1) wap to input user's first name & print its length

first_name = input("enter your first name: ")
print(len(first_name))



# 2) wap to find the occurrence of '$' in a string

str = "samsung $phones $these days are not up to mark"
print(str.count('$'))

# 3) wap to check if num entered by user is odd or even

num = int(input('enter a number: '))

if num % 2 == 0:
    print("even")
else:
    print("odd")


# 4) wap to find the greatest of 3 numbers entered by user

a  = int(input("enter num1: "))
b  = int(input("enter num2: "))
c  = int(input("enter num3: "))

if a > b and a> c:
    print("a is greatest")
elif b > a and b >c:
    print(" b is greatest")
elif c > a and c> b:
    print("c is greatest")
    
#5) wap to check if a number is multiple by 7 or not

num = 50

if num % 7 == 0:
    print("it is multiple")
else:
    print("not multiple")
