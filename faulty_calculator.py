# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:04:41 2022

@author: PERSONAL
"""

x=input("enter either: divide,multiply,add,substract,"  )

num1=int(input("enter first number"))
num2=int(input("enter second number"))

def add(x,y):
    return(x+y)

def substract(x,y):
    return(x-y)
def divide(x,y):
    return(x/y)

def multiply(x,y):
    return(x*y)

if x=="substract":
    print("num1-num2=",substract(num1,num2))
elif x=="add" :
    print(add(num1,num2))
elif x=="divide":

    print(divide(num1,num2))
elif x=="multiply":
    print(multiply(num1,num2)) 

else:
    print("invalid input")








#Use + for addition, - for Subtraction, * for Multiplication, / For Division...
"""
a = input("Operator")
x = int(input("Enter First No."))
y = int(input("Enter Second No."))
print("The Answer is:")
if x== 45 and y==3 and a=="*":
    print("555")
elif x== 56 and y==9 and a=="+":
    print("77")
elif x== 56 and y==6 and a=="/":
    print("4")
elif a== "+" :
    print(x + y)
elif a== "-":
    print(x - y)
elif a== "*":
    print(x * y)
elif a== "/":
    print(x / y)
else:
    print("Syntax Error")
    """
    
    
    
print("choose any operator: *,/,+,-") 

operator=input()
x=int(input("enter first number:"))
y=int(input("enter second number:"))  #45*3= 555,56+9=77,56/6=4

print("the answer is:")

if x==45 and y==3 and operator=="*"or x==3 and y==45 and operator=="*":

    print(555)
elif x==56 and y==9 and operator=="+" or x==9 and y==56 and operator=="+" :
    
    print(77)

elif x==56 and y==6 and operator=="/" or   x==6 and y==56 and operator=="/":
    
    print(4)
    
elif operator=="+":
    print(x+y)
elif operator=="-":
    print(x-y)
elif operator=="/":
    print(x/y)
elif operator=="*":
    print(x*y)
else:
    print("invalid input")    

