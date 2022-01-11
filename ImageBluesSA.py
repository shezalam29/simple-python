#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: September 24th, 2019

 

import numpy as np
import matplotlib.pyplot as plt

n = input('Enter the name of the input file: ')
o = input('Enter the name of the output file: ')
img = plt.imread('csBridge.png')
plt.imshow(img)
plt.show()

sec = img.copy()
sec[:,:,1] = 0
sec[:,:,0] = 0

plt.imshow(sec)
plt.show()

plt.imsave("blueH.png", sec)


