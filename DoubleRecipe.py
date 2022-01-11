#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: October 16th, 2019

import matplotlib.pyplot as plt
import pandas as pd

n = input("Enter recipe name: ")
rec = pd.read_csv(n)
print("Double your recipe is: ")
rec.Amount *= 2
print(rec)




