# Project 1: Snake, Water, Gun Game

import random

computer=random.choice([-1,0,1])
youStr=input("Enter you choice: ")
youDic={"s":1,"w":-1,"g":0}
revDic={1:"Snake",-1:"Water",0:"Gun"}
you=youDic[youStr]

print(f"You choose {revDic[you]} and \nComputer choose {revDic[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("You loose")
    elif(computer == 1 and you == -1):
        print("You loose")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == -1):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You loose")
    else:
        print("Something went wrong")