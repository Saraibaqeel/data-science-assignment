                                                   # Assignment No#1     
#Q1:
 print("Twinkle, twinkle, little star,\n\t How i wonder what you are! \n\t\t up above the world so high  \n\t\t Like a diamond in the sky \ntwinkle twinkle little star \n\thow i wonder what you are!")


#Q2:
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
#Q3:
from datetime import datetime

today=datetime.today()

print("Today Date and time is", today)

#Q4:
r=float (input("Enter radius:"))
PI=3.142
Area=PI*r*r
print("Area =", Area)

#Q5:
fname=input("Enter First name: ")
lname=input("Enter Last name: ")
rfname=fname[::-1]
rlname=lname[::-1]
print(rfname, " ",rlname)

#Q6:

a=input("1st number:")

b=input("2nd number:")
c=float(a)+float(b)
print('Sum =' ,c)
