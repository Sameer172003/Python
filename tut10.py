# Chapter 10 – Object Oriented Programming

# Class - A class is a blueprint for creating objects.
# Object - An object is an instantiation of a class.

class Employee: # Creating a class 
    language="Java" # This is a class attribute
    age=21

sam=Employee() # sam is an object
sam.name="Sameer" # This is an instance attribute
print(sam.name,sam.language,sam.age) 

rohan=Employee()
rohan.name="Rohan"
print(rohan.name,rohan.language,rohan.age)

# Here name is instance attribute and age and language are class attributes as they directly belong to the class

# Function with class and object (Self Parameter)

class Emp:
    regNo=101
    salary=120000

    def getInfo(self):
        print(f"The registration number of the employee is {self.regNo} and the salary is {self.salary}")
    

obj=Emp()
obj.getInfo()

# Mixed Concepts (__init__ method used to make a constructor)

class Car:
    # constructor
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    # Method to display
    def display(self):
        print("Brand: ",self.brand)
        print("Year: ",self.year)


# Object Creation
myCar=Car("Toyota",2020)

myCar.display()


# Example on Static Method

class MathUtils:
    # Static method
    @staticmethod
    def square(x):
        return x * x

# Call static method without creating an object
result = MathUtils.square(5)
print("Square is:", result)


# Why use @staticmethod? ---> No need for self or cls