# Chapter 7 – Loops in Python

# We use loops to do repetitive works

# Types of loops --> 1) for loop 2) while loop

# Example - Write a program to print a number from 1 to 10 using both while and for loops

i=1
while(i<11):
    print(i)
    i=i+1

# print("\n")

for i in range(1,11):
    print(i)

# Use of loops with list

arr=[1,3,7,5,6]

for i in arr:
    print(i)

# Use of loops with list and if-else

for i in arr:
    if(i%2==0):
        print("True")
    else:
        print("False")
    
# Break and Continue Statements

for i in arr:
    if(i%2 == 0):
        break
    else:
        print(i)
    
for i in arr:
    if(i%2!=0):
        continue
    else:
        print(i)

# Take user input and add it in list

array=[]
for i in range(0,4):
    array.append(int(input("Enter num: ")))

for i in array:
    print(i)

