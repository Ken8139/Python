'''Author:kenaz mathukutty 
Created:30/11/2024
Python program '''

def mobile_no():
    n=input("enter")
    if len(n)==10 and (n[0]=="7" or n[0]=="8" or n[0]=="9"):
        print("Valid")
    else:
        print("invalid")

mobile_no()


