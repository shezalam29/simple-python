#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: September 17th, 2019
#This program prompts the user to enter a word and and the prints out the word with each letter shifted right by 13 

n = input('Enter a word ')
print('Your word in code is: ')
for i in n:
    num = ord(i)
    if num >= 109:
        num = num - 13
    else:
        num = num + 13
    ch = chr(num)
    print(ch, end = "")
    
