#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: September 25th, 2019
#1.  Ask the user for the number of seconds until lecture starts.
#2.  Print out the hours until lecture (hours = seconds //3600).
#3.  Compute the remaining seconds (rem = seconds % 3600).
#4.  Print out the minutes until lecture (minutes = rem // 60).
#5.  Print out the remaining seconds (remSec = rem % 60).

n = int(input('Enter the number of seconds before lecture starts '))
hours = n//3600
print('Hours: ', hours)
rem = n%3600
mins= rem//60
print('Minutes: ', mins)
remsec = rem%60
print('Seconds: ', remsec)
