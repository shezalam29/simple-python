#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: October 16th, 2019
import pandas as pd
import matplotlib.pyplot as plt



n = input("Enter name of the input file: ")
m = input("Enter name of the output file: ")
df = pd.read_csv(n)
df["Date"] = pd.to_datetime(df["Date"].apply(str))
df["% Attending"] = ((df["Present"])/(df["Enrolled"])) * 100
df.plot(x = "Date" , y = "% Attending")
new = plt.gcf()
new.savefig(m)

