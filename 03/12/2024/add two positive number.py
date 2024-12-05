'''
python program
Author:Kenaz mathukutty
Created:03/12/2024
'''
def add_number(n1,n2):
    if n2==0:
        return n1
    else:
        return add_number(n1+1,n2-1)
ans=add_number(1,2)
print(ans)