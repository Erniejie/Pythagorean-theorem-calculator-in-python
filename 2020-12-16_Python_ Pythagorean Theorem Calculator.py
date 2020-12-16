##Pythagorean theorem calculator in python-12 December YT - Computer Tutor Program
# c^2 = a^2 + b^2

from math  import sqrt

print ("Pythagoras Theorem Calculator.\n")
print("Right Angle Triangle of Sides <a>,<b>,<c> :\n\n")
Triangle_Side = input("Which Side (a,b,c) to be Calculated ?")

if Triangle_Side == "c":
    sa= int(input("Enter   Side <a> : "))
    sb= int(input("Enter  Side <b> : "))
    sc= sqrt(sa*sa + sb*sb)
    print("The Length of Hypotenuse <c> is : ",sc)

elif Triangle_Side == "a":
    sb= int(input("Enter   Side <b> : "))
    sc= int(input("Enter  Hypotenuse <c> : "))
    sa= sqrt(sc*sc - sb*sb)
    print("The Length of Side <a> is : ",sa)

elif Triangle_Side == "b":
    sa= int(input("Enter   Side <a> : "))
    sc= int(input("Enter  Hypotenuse <c> : "))
    sb= sqrt(sc*sc - sa*sa)
    print("The Length of Side <b> is : ",sb)

else :
    print("Please, Select a side Between<a,b,c> ")
    
    

