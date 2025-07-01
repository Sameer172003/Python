# 1) Create a class named Programmer to store information about a few programmers working at Microsoft.

# Method - 1

class Programmer:
    refID=101
    salary=4500000

a1=Programmer()
a1.name="Sameer"
print(a1.name,a1.refID,a1.salary)

a2=Programmer()
a2.name="Harry"
print(a2.name,a2.refID,a2.salary)

# Method - 2

class Programmer:
    def __init__(self,name,salary,refID):
        self.name=name
        self.salary=salary
        self.refID=refID

b1=Programmer("Sam",1000000,101)
print(b1.name,b1.salary,b1.refID)

b2=Programmer("Harry",1000000,102)
print(b2.name,b2.salary,b2.refID)


# 2) Write a class Calculator that can compute the square, cube, and square root of a number.

import math

class Calculator:
    @staticmethod
    def square(n):
        print(n*n)
    @staticmethod
    def cube(n):
        print(n*n*n)
    @staticmethod
    def sqRoot(n):
        # print(math.sqrt(n))
        print(n**1/2)


Calculator.square(4)
Calculator.cube(4)
Calculator.sqRoot(4)

# 3) Write a class Train with methods to: (i) Book a ticket (ii) Get train status (e.g., number of seats) (iii)Retrieve fare details of trains operating under Indian Railways.

import random

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,source,destination):
        print(f"Ticket is booked in Train Number {self.trainNo} from {source} to {destination}")
    def getStatus(self):
        print(f"Train Number {self.trainNo} is running on time")
    def getFare(self,source,destination):
        print(f"Ticket fair in Train Number {self.trainNo} from {source} to {destination} is {random.randint(500,1000)}")

        
run=Train(12223)
run.book("Howrah","Delhi")
run.getStatus()
run.getFare("Howrah","Delhi")