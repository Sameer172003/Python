# Chapter 1 – Modules, Comments & pip

print("Hello World")

# Modules - A module is a file containing code written by somebody else which can be imported and used in our program.

# Pip - Pip is the package manager for python you can use pip to install a module on your system.

# Example - pip install flask ---> it install flask module in the system

# Types of modules - 1) Built in modules 2) External modules

# Comments - Comments are used to write something which the programmer does not want to execute.

# Types of comments - 1) Single line (#) 2) Multi line ("""......""")

# Adding a module

# pip install pyttsx3

import pyttsx3
engine=pyttsx3.init()
engine.say("Hello My Name is Sameer")
engine.runAndWait()
