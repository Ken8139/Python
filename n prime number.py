'''
Python Lab
Author=Kenaz mathukutty
Date=15/10/2024
python program
'''

limit=int(input("Enter a number"))
for number in range(2,limit+1):
    isprime= True
    for i in range(2,(number//2)+1):
        if number% i==0:
            isprime= False
    if isprime:
        print(number)


