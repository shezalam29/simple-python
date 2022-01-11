#Shezan Alam
#shezan.alam48@myhunter.cuny.edu
#November 4th

binString = str(input('Enter binary number: '))
decNum = 0
for i in binString:
    decNum = decNum*2
    if int(i) == 1:
        decNum = decNum + 1
print("Your number in decimal is" , decNum)
