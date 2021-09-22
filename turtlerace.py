import time
import random
import turtle
from turtle import Turtle

#window setup
window = turtle.Screen()
window.title("turtle race")
window.setup(800, 800)
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write("TURTLE RACE", font=("Arial", 30, "bold"))
turtle.penup()

#ground
turtle.setpos(-400, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.end_fill()

#destination
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10) :
    turtle.setpos(finish_line, (150-(i * square_size *2)))
    turtle.stamp()

for j in range(10) :
    turtle.setpos(finish_line+square_size, ((150-square_size) - (j*square_size*2)))
    turtle.stamp()
    
turtle.hideturtle()
             
# turtle1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()

# turtle2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("white")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

# turtle3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("red")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

# turtle4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("cyan")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

time.sleep(1)

for i in range  (145):
    turtle1.forward(random.randint(1,5))
    turtle2.forward(random.randint(1,5))
    turtle3.forward(random.randint(1,5))
    turtle4.forward(random.randint(1,5))
                    
turtle.exitonclick()











