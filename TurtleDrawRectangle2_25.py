#Draw Rectangle based on user input of center, width and SCREENHEIGHT

import turtle

x,y = eval(input("Enter co-ordinates for center of the rectangle : "))
h = eval(input("Enter height of rectangle :" ))
w = eval(input("Enter width of rectangle : "))

turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.goto(x,y)
center = turtle.pos()
turtle.write(center)
turtle.dot(3)
turtle.penup()
turtle.left(90)
turtle.forward(h/2)
turtle.left(90)
turtle.forward(w/2)
turtle.right(180)
turtle.pendown()
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h)

turtle.exitonclick()