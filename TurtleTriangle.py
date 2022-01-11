#Shezan Alam
#November 10th, 2019
#shezan.alam48@myhunter.cuny.edu

def triangle(t,length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t,(length/2))

def nestedTriangle(t,length):
    if length >10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t,(length/2))
