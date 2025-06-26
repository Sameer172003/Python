# Chapter 3 – Strings

# String is a datatypes in a python
# String is a sequence of characters enclosed in a quotes

name="Sameer"

# len() function

print(len(name))

# String Slicing

# name[SI : EI]

print(name[1:5])

# name[SI:EI:SI]

word="amazing"

print(word[1:6:2])

# String endswith & startwith

print(name.endswith("eer"))

print(name.startswith("Sa"))

# String capitalize

print(word.capitalize())
print(word.upper())
print(word.lower())

# String find

s="hello world"
index=s.find("world")
print(index)

# String count

cnt=s.count("l")
print(cnt)

# String replace

new=s.replace("world","sameer")
print(new)

# Escape Sequence 

# 1) \n --> new line 2) \t --> tab space 3) \\ --> backslash  4) \' --> single quotes

print("Hello my name is \nsameer")

# Some extra knowledge

str=input("Enter your name:")
print(f"Good night, {str}")

# Finding double spaces in string

s1="Hello my name is  Sameer"
print(s1.find("  "))