#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: September 25thth, 2019

import matplotlib.pyplot as plt
import numpy as np
logoImg = np.ones((30,30,3))

logoImg[:,:10,:2] = .5 #left third


logoImg[:10,:,:2] = .5 #top third

logoImg[20:30,:,:2] = .5 #bottom third

plt.imshow(logoImg)
plt.show()
plt.imsave("logo.png", logoImg)


