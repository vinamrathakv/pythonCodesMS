import turtle
import math

turtle.speed(0) # Fastest  

# Draw X-axis
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
turtle.goto(150, 0)

# Draw Y-axis
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.goto(0, 100)

# Display X
turtle.penup()
turtle.goto(10, 110)
turtle.pendown()
turtle.write("Y") 
            
# Display Y
turtle.penup()
turtle.goto(180, -15)
turtle.pendown()
turtle.write("X") 

# Draw arrows

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
turtle.setheading(150)
turtle.forward(20)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.setheading(240)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.setheading(-60)
turtle.forward(20) 

# Draw a square function
scaleFactor = 0.01
left = -50
right = 50
x = left
turtle.penup()
turtle.goto(x, 0.05 * x * x)
turtle.pendown()
for  x in range(left, right + 1):
    turtle.goto(x, 0.05 * x * x)



turtle.hideturtle()

turtle.done()