#Shezan Alam
#shezan.alam48@myhunter.cuny.edu
#November 4th

import pandas as pd

csvFile = input('Enter file name: ')         
filmP = pd.read_csv(csvFile)
x = (filmP.shape[0])
print('There were' , x , 'film permits.')
m = filmP['Borough'].value_counts()
print(m)

p = filmP["ParkingHeld"].value_counts()[:5]
print('The five most popular filming locations were:' , p)

