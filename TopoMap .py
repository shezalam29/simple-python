#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: October 9th, 2019


import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')


mapShape = elevations.shape + (3,)

newMap = np.ones(mapShape)

blue = float(input('How blue is the ocean: '))

n = str(input('What is the output file: '))

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
           newMap[row,col,2] = blue
           newMap[row,col,0] = 0
           newMap[row,col,1] = 0
           
        if (elevations[row,col] % 10 == 0) & (elevations[row,col] > 0):
           newMap[row,col,0] = 0
           newMap[row,col,1] = 0
           newMap[row,col,2] = 0

           



print('Thank you for using my program!')
print('Your map is stored' , n)

    
        

