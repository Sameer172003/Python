# Chapter 8 – Functions & Recursions

# A function is a group of statements that helps to performing a specific task

# Example -

def avg(): # Function Definition
    a=int(input("Enter any number: "))
    b=int(input("Enter any number: "))
    c=int(input("Enter any number: "))

    average=(a+b+c)/3
    print(average)

avg() # Function Call

# Function with arguments (1 way)

def goodDay(name):
    print("Good day, "+ name)

goodDay("Sameer")

# Function with arguments (2 way)

def goodBye(name):
    gr="Good bye, "+ name
    return gr

ans=goodBye("Sameer")
print(ans)

# Default parameters 

def wish(name,end="Thank you"):
    print("Good Luck, "+ name)
    print(end)

wish("Sameer")

# Recursion - A function call itself is called recursion

# Example of factorial problem using recursion

def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)

res=fact(3)
print(res)

# Example of fibonacci series using recursion

def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)

result=fib(4)
print(result)
