#Shezan Alam
#shezan.alam48@myhunter.cuny.edu
import turtle
import pandas as pd

def setup(windowTitle):
    
    screen = turtle.Screen()
    screen.title(windowTitle)

    # this assures that the size of the screen will match the map image:
    screen.setup(800, 404)
    #Set coordinates for latitude and longitude:
    screen.setworldcoordinates(-180,-90,180,90)

    # ... which is the same size as our image
    # now set the background to our space image
    screen.bgpic("mapNASA.gif")

    t = turtle.Turtle()
    t.pensize(1)
    t.color('red')
    t.penup()

    return t,screen

def animate(t,lat,lon,wind):
   
    if wind>157:
        t.color("red")
        t.pensize(5)
        t.goto(lon,lat)
        t.pendown()
        
    if (wind > 130) and (wind <156):
        t.color("orange")
        t.pensize(4)
        t.goto(lon,lat)
        t.pendown()
        
    if (wind > 111) and (wind < 129):
        t.color("yellow")
        t.pensize(3)
        t.goto(lon,lat)
        t.pendown()
        
    if (wind > 96) and (wind < 110):
        t.color("green")
        t.pensize(2)
        t.goto(lon,lat)
        t.pendown()
        t.penup()
    if (wind > 74) and (wind < 95):
        t.color("blue")
        t.pensize(1)
        t.goto(lon,lat)
        t.pendown()
       
    if (wind < 75):
        t.color("white")
        t.pensize(1)
        t.goto(lon,lat)
        t.pendown()
        

    return(t)

def main():
    """Animates the path of hurricane from file:
    """
    hFile = input('Enter file name: ')
    t, wn = setup(hFile)

    df = pd.read_csv(hFile)
    for index,row in df.iterrows():
        lat = int(row["Lat"])
        lon = int(row["Lon"])
        wind = row["Wind"]
        print(lat,lon,wind)
        animate(t,lat,lon,wind)

if __name__ == "__main__":
    main()
