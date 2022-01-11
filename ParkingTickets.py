#Shezan Alam
#shezan.alam48@myhunter.cuny.edu    
#October 31st, 2019

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter file name: ')         #Name of the CSV file
att = input('Enter attribute: ')
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[att].value_counts()[:10]) #Print out the dataframe
