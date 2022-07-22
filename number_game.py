# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:07:02 2022

@author: PERSONAL
"""

import random

secret_number = random.randint(5,15)

x = int(input("Guess a number between 5 to 15:"))
    
if (x == secret_number):
         print("player wins and computer loses")
  
        
        
else:
         print("player loses and computer wins")
         
         
while(True):
    datastore=()
    secret=random.randint(1,10)
    x=input("guess a number between 1 and 10:")
    x=int(x)
    

    if (x==secret):
        print("player wins and computer loses")
    else:
        print("computer wins and player loses,try again")
        
    