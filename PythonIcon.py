import turtle
turtle.bgcolor('black')
def leftcurve(x,y,z):
    for i in range(x):
        turtle.left(y)
        turtle.forward(z)
def rightcurve(x,y,z):
    for i in range(x):
        turtle.right(y)
        turtle.forward(z)
turtle.fillcolor('royalblue')
turtle.begin_fill()
turtle.pensize(5)
turtle.pencolor('white')
turtle.forward(20) 
turtle.left(90)
turtle.forward(15)
rightcurve(32,3,1)
turtle.left(6)
turtle.forward(40)
leftcurve(32,3,1) 
turtle.right(6)
turtle.forward(30)
turtle.left(70)
leftcurve(12,3,6)
turtle.left(75)
turtle.forward(30)
turtle.left(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(75)
leftcurve(32,3,1)
turtle.right(6)
turtle.forward(12)
leftcurve(32,3,1)
turtle.end_fill()
turtle.penup()
turtle.pencolor('white')
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(120)
turtle.left(84)
turtle.forward(60)
turtle.left(90)
turtle.pencolor('white')
turtle.pendown()
turtle.pensize(5)
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.forward(20)
turtle.left(90)
turtle.forward(15)
rightcurve(32,3,1)
turtle.left(6)
turtle.forward(40)
leftcurve(32,3,1)
turtle.right(6)
turtle.forward(30)
turtle.left(70)
leftcurve(12,3,6)
turtle.left(75)
turtle.forward(30)
turtle.left(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(75)
leftcurve(32,3,1)
turtle.right(6)
turtle.forward(12)
leftcurve(32,3,1)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(50)
turtle.pendown()
turtle.pencolor('white')
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()
turtle.right(80)
turtle.penup()
turtle.forward(78)
turtle.pendown()
turtle.circle(3)
turtle.penup()
turtle.forward(100)
turtle.done()
