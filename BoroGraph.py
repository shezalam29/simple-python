#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: October 4th, 2019
import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop.plot(x="Year")

n = input("Enter borough name: ")
o = input("Enter output name: ")

pop['Fraction'] = pop[n]/pop['Total']
pop.plot(x='Year' , y= 'Fraction')
fig = plt.gcf()
fig.savefig(o)

