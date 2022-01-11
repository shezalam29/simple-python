#Shezan Alam
#shezan.alam48@myhunter.cuny.edu

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(30)
  a = random.randrange(0,350,10)
  trey.left(a)
