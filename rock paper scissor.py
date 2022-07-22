# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:08:32 2022

@author: PERSONAL
"""

import random
possible=["rock","paper","scissor"]
computer=random.choice(possible)
print(" Rock wins against scissors; paper wins against rock; and scissors wins against paper.If both players, it is considered a tie and play resumes until there is a clear winner. ")
x=input("Enter either rock,paper or scissor:")
x=str(x)

if(x==computer):
    print("its a tie")
elif (x=="rock"):
    if (computer=="scissor"):
        print("rock smashes scissor,you win!")
    else:
        print("paper covers rock,you lose!")
elif (x=="scissor") :
    if (computer=="paper") :
        print("scissor cut the paper, you wins!")
    else:
        print("rock smashes scissor,you lose")
        
elif (x=="paper") :
    if (computer=="rock"):
        print("paper covers rock,you wins")
    else:
        print("scissor cuts paper,you lose")    
        
#2
while(True):
    import random
    possible=["rock","paper","scissor"]
    computer=random.choice(possible)
    print(" Rock wins against scissors; paper wins against rock; and scissors wins against paper.If both players, it is considered a tie and play resumes until there is a clear winner. ")
    x=input("Enter either rock,paper or scissor:")
   
            
    
   
    if(x==computer):
        print("its a tie")
    elif (x=="rock"):
        if (computer=="scissor"):
            print("rock smashes scissor,you win!")
        else:
            print("paper covers rock,you lose!")
    elif (x=="scissor") :
        if (computer=="paper") :
            print("scissor cut the paper, you wins!")
        else:
            print("rock smashes scissor,you lose")
            
    elif (x=="paper") :
        if (computer=="rock"):
            print("paper covers rock,you wins")
        else:
            print("scissor cuts paper,you lose")  
            
   
       
        