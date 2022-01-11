#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: October 16th, 2019
import pandas as pd
import matplotlib.pyplot as plt



n = input("Enter name of the input file: ")
homeless = pd.read_csv(n)
o = input("Enter name of the output file: ")
homeless['Fraction Children'] = (homeless["Total Children in Shelter"])/(homeless["Total Individuals in Shelter"])
homeless.plot(x = "Date of Census" , y = "Fraction Children")
new = plt.gcf()
new.savefig(o)


