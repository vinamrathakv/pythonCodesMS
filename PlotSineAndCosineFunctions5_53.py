import turtle
import math

turtle.speed(0) # Fastest  

# Draw X-axis
turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()
turtle.goto(250, 0)

# Draw Y-axis
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.goto(0, 150)

# Display Y
turtle.penup()
turtle.goto(10, 150)
turtle.pendown()
turtle.write("Y") 
            
# Display X
turtle.penup()
turtle.goto(250, -15)
turtle.pendown()
turtle.write("X") 

# Draw arrows

turtle.penup()
turtle.goto(250, 0)
turtle.pendown()
turtle.setheading(150)
turtle.forward(20)

turtle.penup()
turtle.goto(250, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 150)
turtle.pendown()
turtle.setheading(240)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 150)
turtle.pendown()
turtle.setheading(-60)
turtle.forward(20)

turtle.speed(0)
#Plot Sine function
turtle.color("blue")
turtle.penup()
for angle in range(-360,361):
    
    y = math.sin(math.radians(angle))
    
    turtle.goto(.5 * angle, y * 80)
    turtle.pendown()
    
#Plot Cosine function
turtle.color("red")
turtle.penup()
for angle in range(-360,361):
    
    y = math.cos(math.radians(angle))
    
    turtle.goto(.5 * angle, y * 80)
    turtle.pendown()

