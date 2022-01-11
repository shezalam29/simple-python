#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: September 17th, 2019
#This program prompts the user for a DNA string, and then prints the length and the GC-content as a decimal

n = input('Enter a DNA string: ')
num = len(n)
print ("Length is " , num)

numC = n.count('C')
numG = n.count('G')
numTotal = numC + numG

per = numTotal/num
print ("GC-content is " , per)
