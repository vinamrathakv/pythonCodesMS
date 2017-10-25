# Check if 2nd circle is inside the first circle or overlaps with first FillingCirclesBar
import math


# get user input for both the circles' co-ordinates and radii

x1, y1, r1 = eval(input("Enter the x co-ordinate, y co-ordinate and radius of circle 1 : "))
x2, y2, r2 = eval(input("Enter the x co-ordinate, y co-ordinate and radius of circle 2 : "))

distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)     #calculate distance between the centers of the two circles

if(distance <= math.fabs(r1-r2)):                       #check if centers are closer than or equal to difference in radii
    if(r1 > r2):                                        # if r1 is greater than r2, second circle is insede first circle
        print("The second circle is inside the first circle.")
        
    if(r2 > r1):                                        # if r2 is greater than r1, first circle is inside second circle
        print("The first circle is inside the second circle")
    
elif(distance <= math.fabs(r1+r2)):                     #check if distance between centers is less than or equal to sum of radii
    print("The second circle overlaps with the first circle.")
    
elif(distance > math.fabs(r1+r2)):                      # check if distance between centers is greater than sum of radii
    print("The second circle is completely outside the first circle")