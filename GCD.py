'''
python program
Author:Kenaz mathukutty
Created:03/12/2024
'''
python program
author: Kenaz mathukutty
Created: 03/12/1014
def GCD_number(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return GCD_number(n2,n1%n2)
f=GCD_number(516,188)
print(f)