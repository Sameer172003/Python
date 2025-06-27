# 1) Write a program to print the multiplication table of a given number using a for loop

n=int(input("Enter any number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

# 2) Write a program to calculate the sum of the first n natural numbers.

n1=int(input("Enter any number: "))
sum=0
for i in range(1,n1+1):
    sum=sum+i

print(sum)

# 3) Write a program to compute the factorial of a given number.

n2=int(input("Enter any number: "))
fac=1
for i in range(1,n2+1):
    fac=fac*i

print(fac)

# 4) Write a program to determine whether a given number is prime or not.

n4=int(input("Enter any number: "))

if(n4<=1):
    print("NOT PRIME")

for i in range(2,n4):
    if(n4%i==0):
        print("NOT PRIME")
        break
    else:
        print("PRIME")
        break