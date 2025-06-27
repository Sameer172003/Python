# Chapter 6 – Conditional Expression

# "if-else & elif" conditional expressions in python

a1=8
if(a1>10):
    print("Greater")
elif(a1==10):
    print("Equal")
else:
    print("Lower")


# 1) Write a program to find the greatest among four numbers entered by the user.

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))
d=int(input("Enter num4: "))

if(a>b and a>c and a>d):
    print("A is greater than all")
elif(b>a and b>c and b>d):
    print("B is greater than all")
elif(c>a and c> b and c>d):
    print("C is greater than all")
else:
    print("D is greater than all")

# 2) Write a program to check whether a given username contains fewer than 10 characters.

str="Sameer ojha"
if(len(str) > 10):
    print("True")
else:
    print("False")

# 3) Write a program to check whether a given name is present in a list or not.

arr=["sam","ram","shyam","rahul"]
ans=input("Enter any name: ")
if(ans in arr):
    print("Present")
else:
    print("Absent")





