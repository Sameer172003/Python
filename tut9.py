# Chapter 9 – File I/O

# A file is stored in a storage device. A python program can talk to the file by reading content from it and writing content from it.

# Types of files - 1) Text files (.txt, .c etc) 2) Binary files (.jpg etc)

# Reading a file in python 
 
file=open("f.txt","r")
data=file.read()
print(data)
file.close() 

# Writing a file in python

st="Hey, My name is Sameer and I am a Software Engineer"

file2=open("f2.txt","w")
file2.write(st)
file2.close()
