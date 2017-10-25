# display if circles overlap or not using turtle 

import turtle
import math

# get user input for both the circls' co-ordinates and radii

x1, y1, r1 = eval(input("Enter the x co-ordinate, y co-ordinate and radius of circle 1 : "))
x2, y2, r2 = eval(input("Enter the x co-ordinate, y co-ordinate and radius of circle 2 : "))

turtle.penup()
turtle.goto(x1,y1)
turtle.right(90)            #point south
turtle.forward(r1)          #move down equal to radius
turtle.right(270)           #turn east
turtle.pendown()
turtle.pensize(4)
turtle.color("teal")        #draw circle with specified coordinates as center
turtle.circle(r1)
turtle.penup()
turtle.goto(x2,y2)
turtle.right(90)
turtle.forward(r2)
turtle.right(270)
turtle.pendown()
turtle.color("purple")
turtle.circle(r2)
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.color("red")

distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2) 
print("Distance between centers : ",distance)    #calculate distance between the centers of the two circles

if(distance <= math.fabs(r1-r2)):                       #check if centers are closer than or equal to difference in radii
    if(r1 > r2):                                        # if r1 is greater than r2, second circle is insede first circle
        turtle.write("The second circle is inside first circle")                                      
        
        
    if(r2 > r1):                                        # if r2 is greater than r1, first circle is inside second circle
        turtle.write("The first circle is inside second circle")     
    
elif(distance <= math.fabs(r1+r2)):                     #check if distance between centers is less than or equal to sum of radii
    turtle.write("The circles overlap")                     
       
elif(distance > math.fabs(r1+r2)):                      # check if distance between centers is greater than sum of radii
    turtle.write("The circles do not overlap")  
                      
turtle.penup()    
turtle.goto(0,0)
turtle.exitonclick()