#Shezan Alam
#shezan.alam48@myhunter.cuny.edu
#November 4th

def computeFare(zone, ticketType):

    fare = 0
    if (zone ==2) or (zone==1):
        if (ticketType == "adult"):
            fare = 23
        else:
            fare = 11.5
    elif (zone ==3):
        if (ticketType == "adult"):
            fare = 34.5
        else:
            fare = 23
    elif (zone ==4):
        if (ticketType == "adult"):
            fare = 46
        else:
            fare = 23
    else:
        fare = -1 
  
     
     
    return(fare)
