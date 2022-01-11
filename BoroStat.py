#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: October 16th, 2019
import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv',skiprows=5)


n = input("Enter borough: ")

mi = pop[n].min()
av = pop[n].mean()
ma = pop[n].max()

print("Minimum population: ", mi)
print("Average population: ", av)
print("Maximum population: ", ma)

