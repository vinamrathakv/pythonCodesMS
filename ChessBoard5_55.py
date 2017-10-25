import turtle

start_x = -50
start_y = 50
length = 20
count = 1

x = start_x
y = start_y
turtle.speed(0)

for j in range(0,8):
    
    
    
    for i in range(1,9):
    
        turtle.penup()
        turtle.goto(x,y)
        if count % 2 != 0:
            turtle.color("black", "white")
        
        else:
            turtle.color("black")

        turtle.seth(0)
        turtle.left(90)
        turtle.begin_fill()
        turtle.pendown()
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.end_fill()
        turtle.penup()
        count += 1
    
        if (i == 9):
            break
        
        else:
            x += length
    count = count + 1        
    y = y-length
    x = start_x

turtle.exitonclick()
              