#Shezan Alam
#shezan.alam48@myhunter.cuny.edu

def convert(s):
     """ Takes a hex string as input.
     Returns decimal equivalent.
     """

     total = 0
     
     for c in s:
          total = total * 16
          asci = ord(c)
          if ord('0') <= asci <= ord('9'):
               #It's a decimal number, and return it as decimal:
               total = total+asci - ord('0')
          elif ord('A') <= asci <= ord('F'):
               #It's a hex number between 10 and 15, convert and return:
               total = total + asci - ord('A') + 10
          elif ord('a') <= asci <= ord('f'):
               #Check if they used lower case:
               #It's a hex number between 10 and 15, convert and return:
               total = total + asci - ord('a') +++ 10
          else:
               #Not a valid number!
               return(-1)
     return(total)

def main():
    hexString = input("Enter a number in hex: ")
    print("The number in decimal is", convert(hexString))


#Allow script to be run directly:
if __name__ == "__main__":
     main()
 
