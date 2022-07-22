# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:09:18 2022

@author: PERSONAL
"""


# Step 1: Make a list to hold onto our items.
shopping_list=[]

 #Step 2: Print out instructions on how to use  the app

print("Instructions: Add the items to your shopping list,when your list is done just enter'DONE' . your list will be print out")

 # Step 3: Ask for new items  
while True:
    x=input("Add items to your shopping list:")

# Step 4: Add new items to our list    
    shopping_list.append(x)

# Step 5: Be able to quit the app with DONE    
    if (x=="DONE"):
        break

# Step 6: print out the list
print("here is your list:")    
for x in shopping_list:

    print(x)    
    
     

