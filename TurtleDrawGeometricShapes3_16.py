#Draw simple shapes using turtle
import turtle

turtle.pensize(4)
turtle.penup()
turtle.goto(-90,0)
turtle.pendown()
turtle.seth(60)
turtle.begin_fill()
turtle.color("lavender")
turtle.circle(50,steps = 3)
turtle.end_fill()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.seth(45)
turtle.begin_fill()
turtle.color("light green")
turtle.circle(50,steps = 4)
turtle.end_fill()
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.seth(36)
turtle.begin_fill()
turtle.color("light pink")
turtle.circle(50,steps = 5)
turtle.end_fill()
turtle.penup()
turtle.goto(215,0)
turtle.pendown()
turtle.seth(30)
turtle.begin_fill()
turtle.color("gray")
turtle.circle(50,steps = 6)
turtle.end_fill()
turtle.penup()
turtle.goto(325,0)
turtle.pendown()
turtle.seth(22.5)
turtle.begin_fill()
turtle.color("light blue")
turtle.circle(50,steps = 8)
turtle.end_fill()

turtle.exitonclick()