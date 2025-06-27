# Chapter 4 – Lists and Tuples

# Lists are used to store a set of values of any data types. It is mutable

friend=["Apple","Orange",5,45.6,False,"Sameer"]

# Indexing
print(friend[0])
# Assigning other value
friend[0]="Banana"
print(friend[0])

# List Methods
arr=[3,2,5,4,1,6]

# => len() function

print(len(arr))

# 1) Sort
arr.sort()
print(arr)

# 2) Reverse
arr.reverse()
print(arr)

# 3) Append
arr.append(0)
print(arr)

# 4) Insert
arr.insert(0,7)
print(arr)

# 5) Pop
arr.pop(0)
print(arr)

# 6) Remove
arr.remove(0)
print(arr)

# Tuples - A tuple is an immutable data type in a python

a=(1,2,3,4,2,5,2)

# Methods of Tuple

# 1) Count
print(a.count(2))

# 2) Index
print(a.index(5))

# 3) Min and Max
print(min(a))
print(max(a))

# Write a program that takes 3 user input strings and stores it in list

name=[]
n1=input("Enter 1st name: ")
name.append(n1)

n2=input("Enter 2nd name: ")
name.append(n2)

n3=input("Enter 3rd name: ")
name.append(n3)

print(name)

# Write a program that takes 3 user input number and stores it in list and display in sorted manner

array=[]
a1=int(input("Enter num1: "))
array.append(a1)

a2=int(input("Enter num2: "))
array.append(a2)

a3=int(input("Enter num3: "))
array.append(a3)

array.sort()
print(array)

# Write a program to sum a list with 4 numbers

array2=[2,1,4,5]
print(array2[0]+array2[1]+array2[2]+array2[3])
print(sum(array2))
