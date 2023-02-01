import os
import random
print("###### WELCOME TO RPS######")
user_score=0
comp_score=0
ties=0
name=input("enter your name here:")
print("""
Winning rules
1. paper vs rock-->paper
2. rock vs scissors-->rock
3. scissors vs paper-->scissors
""")
while True:
    print(""" The choices are
    1. Rock
    2. Paper
    3. Scissors
    """)
    choice=int(input("enter your choice from 1-3:"))
    print()
    while choice >3 or choice < 1:
        choice=int(input("enter valid input"))
    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Paper"
    else :
        user_choice="Scissors"
    print(name,"'s choice is",user_choice)
    print("now it is computer's turn")
    computer= random.randint(1,3)
    if computer==1:
        comp_choice="Rock"
    elif computer==2:
        comp_choice="Paper"
    else :
        comp_choice="Scissors"
    print("computer choice is",comp_choice)         
    if((user_choice=="Papaer" and comp_choice=="Rock") or( user_choice=="Rock" and comp_choice=="Paper")):    
       print("Paper win")
       resuit="paper"
    elif((user_choice=="Rock" and comp_choice=="Scissors") or( user_choice=="scissors" and comp_choice=="Rock")):
        print("Rock Win")
        result="Rock"
    elif(user_choice==comp_choice):
        print("it is a tie")
        result="Ties"
    else:
        print("scissors wins")
        result="scissors"
    if result=="Ties":
        ties+=1
    elif result== user_choice:
        print(name,"WIN")
        user_score +=1
    else:
        print("COMPUTER WIN")
        comp_score +=1
    print("score are")
    print(name,"'s score is",user_score)
    print("computer's score",comp_score)
    print("ties are",ties)

    repeat=input("do you want to play again?")
    if repeat=="n" or repeat=="no":
        break
print("Game Over")
print("Thank You!")



        







 