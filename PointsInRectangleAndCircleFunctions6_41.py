import turtle
import random

def drawRectangle(x, y, width, height):
    turtle.penup()
    turtle.goto((x - width/2), (y - height/2))
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    
def drawCircle(x, y, radius):
    turtle.seth(0)
    turtle.penup()
    turtle.goto(x, y-radius)
    turtle.pendown()
    turtle.circle(radius)
    
def drawPoint(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()
    
    
x1, y1, = eval(input("Enter the co-ordinates for center of the rectangle : "))
width, height = eval(input("Enter the width and height of the rectangle : "))
x2, y2 = eval(input("Enter the coordinates for center of the circle : "))
radius = eval(input("Enter the radius of the circle : "))

turtle.speed(8)

drawRectangle(x1, y1, width, height)
drawCircle(x2, y2, radius)


count = 0
while(count < 10):
    
    x3 = random.randint((x2- radius + 2), (x2 + radius -2))
    y3 = random.randint((y2 - radius + 2), (y2 + radius - 2))
    if(((x2-x3)**2 + (y2-y3)**2)**0.5) < radius-3 :
        
        drawPoint(x3, y3)
        
        x3 = random.randint((x1- width/2 + 3), (x1 + width/2 -3))
        y3 = random.randint((y1 - height/2 +3), (y1 + height/2 -3))
        drawPoint(x3, y3)
        
        count += 1
turtle.hideturtle()
turtle.done()
                        
                        
