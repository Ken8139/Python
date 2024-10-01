'''Author: kenaz mathukutty
Date: 01/10/2024
Version: 1.0
Python program to get the student details
'''
name=input("Enter your name of the student")
roll_number=int(input("Enter Roll Number"))
roll_number=roll_number+1
CGPA=float(input("enter your CGPA"))
percentage_mark=CGPA*100
print("Name of the sudent:",name)
print("Roll number",roll_number)
print("Mark percentage",percentage_mark,"%")