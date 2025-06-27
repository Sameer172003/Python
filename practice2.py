# 1) Write a program using a function to find the greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

ans=greatest(1,2,3)
print(ans)

# 2) Write a Python program using a function to convert Celsius to Fahrenheit.

def conv(temp):
    return (temp*1.8)+32

res=conv(27)
print(res)

# 3) Write a recursive function to calculate the sum of the first n natural numbers.

def add(n):
    if(n==1):
        return 1
    else:
        return n+add(n-1)

answer=add(10)
print(answer)
