'''
Python Lab
Author=Kenaz mathukutty
Date=15/10/2024
python program
'''
    
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if num1<num2 and num1<num3:
    print("The smallest:",num1,"smallest")
elif num2<num3 and num2<num1:
    print("The smallest:",num2,"smallest")
else:
    print("The smallest:",num3,"is smallest ")