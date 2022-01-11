#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: September 25th, 2019

#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')
plt.imshow(elevations)
plt.show()
#Take the shape (dimensions) of the elevations
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = 1.0     #Set the blue channel to 100%
        elif elevations[row,col] <= 6:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0     #Set the red channel to 100%
        elif elevations[row,col] > 6 and elevations[row,col] <= 20: 
            floodMap[row,col,0] = .5
            floodMap[row,col,1] = .5
            floodMap[row,col,2] = .5
            
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%


#Save the image:
plt.imsave('floodMap.png', floodMap)
