'''
python program
Author:Kenaz mathukutty
Created:03/12/2024
'''
def factorial (n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
t=factorial(5)
print(t)