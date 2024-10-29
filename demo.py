'''
Python Lab
Author=Kenaz mathukutty
Date=29/10/2024
python program
'''

string_input=input("Enter a string")
vowels="aeiouAEIOU"

vowels_count=0
constanece_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
    else:
        constanece_count+=1
print(f"Number of vowels in the given string {string_input}={vowels_count} \n Number of constanece {constanece_count}")
