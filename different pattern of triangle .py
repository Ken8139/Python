'''
python program
Author: Kenaz mathukutty
Created: 19/11/2024
'''

lim=int(input("Enter the number of start: "))
print("Increasing function")
for i in range(lim+1):
    for j in range(i):
        print("*",end="")
    print()
print("\n Decreasing pattern\t")
for i in range(lim,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print("\n Hill pattern\t")
for i in range(1,lim+1):
    for j in range(lim-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
print("\nReverse hill pattern\t")
for i in range(lim,0,-1):
    for j in range(lim-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()