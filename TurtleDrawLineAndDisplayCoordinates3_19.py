# Draw line and display it's end points

import turtle
# Prompt the user for inputting two points

x1, y1 = eval(input("Enter co-ordinates for point 1: ")) 
x2, y2 = eval(input("Enter co-ordinates for point 2: ")) 
               
# Calculate the distance 

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 

# Display two points and the line 

turtle.penup() 
turtle.goto(x1, y1) 
turtle.pendown()
point_1 = turtle.pos()                          #get position of point_1 
turtle.write(point_1)
turtle.goto(x2, y2)     
point_2 = turtle.pos()                          #get position of point_2
turtle.write(point_2) 
turtle.penup() 
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)       #go to the center of the line
turtle.write(round(distance,2)) 
turtle.exitonclick() 
 