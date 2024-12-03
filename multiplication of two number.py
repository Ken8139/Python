'''
python program
Author:Kenaz mathukutty
Created:03/12/2024
'''
def multi_number(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multi_number(n1,n2-1)
ans=multi_number(2,3)
print(ans)
