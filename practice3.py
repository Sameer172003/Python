# # 1) Write a program to read the content of a file named poems.txt and check whether it contains the word "twinkle".

file=open("poems.txt","r")
data=file.read()
if("twinkle" in data):
    print("True")
else:
    print("False")
file.close()


# # 2) A function named game() in a program allows the user to play a game and returns the score as an integer. You are required to: Read a file named hiscore.txt which either contains the previous high score or is blank. Write a program to update the high score in the file whenever game() returns a score greater than the existing high score.

import random

def game():
    print("You are playing the game...")
    score=random.randint(1,60)
    # Fetch the high score
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore != ""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score {score}")
    if(score > hiscore):
        # write this high score in hiscore.txt
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score

game()

# 3) Write a program to generate multiplication tables from 2 to 20 and save each table in a separate file. Store all these files in a folder suitable for a 13-year-old.

import os

# Create a folder named 'tables' if it doesn't already exist
os.makedirs("tables", exist_ok=True)

def genTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2,21):
    genTable(i)


# 4) A file contains the word "Donkey" multiple times. Write a program to replace every occurrence of this word with "######" by updating the same file.

word ="Donkey"

with open("donkey.txt") as f:
    content=f.read()

contentNew=content.replace(word,"######")


with open("donkey.txt","w") as f:
    f.write(contentNew)


# 5) Write a program to find and display the line numbers where the word "python" appears in the log file.


with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No Python is not present")


# 6) Write a program to make a copy of a text file named "this.txt".

with open("this.txt") as f:
    data=f.read()

with open("copy_this.txt","w") as f:
    f.write(data)




