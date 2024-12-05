'''
Python program
Author: Kenaz mathukutty
Created: 3/12/2024
'''
import random
print("Welcome to the show")
doors=[1,2,3]
host=random.choice(doors)
participant=int(input("Please select a door"))
if participant==host:
    print("You won")
else:
    print("You have chose wrong option")
    reply=input("Do you want to change the option ")
    if reply==' yes':
        revised = int(input("Select another option "))
        if revised==host:
            print("You won")
        else:
            print("You have got goat again,you loose ")
    if reply=='no':
        print("You have got a goat,so you lose")    





