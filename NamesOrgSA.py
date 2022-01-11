#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: October 4th, 2019

names = str(input("Please enter your list of names: "))
namesList = (names.split('; '))

print('You entered: ')
      
for name in namesList:
    str = name.split(",")
    x = str[1]
    y = x[1] + "."
    z = str[0]
    print(y,z)

print("Thank you for using my name organizer!")
