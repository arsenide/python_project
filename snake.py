import turtle
import random

scr = turtle.Screen( )
scr.setup(700, 700)
scr.title("Snake Game!")
scr.bgcolor("blue")

line = turtle.Turtle( ) # 경계선 그리기
line.color("orange")
line.penup( )
line.goto(-300, -300)
line.pendown( )
for i in range(4):
    line.ht( )
    line.forward(600)
    line.left(90)

t = turtle.Turtle( ) # 거북
t.shape("turtle")
t.color ("white")
t.penup( )

food = turtle.Turtle( ) # 먹이
food.shape("circle")
food.color("Red")
food.penup( )
food.speed(0)
food.goto(-100, 100)

def left ( ) :
    t.setheading (180)

def right ( ) :
    t.setheading (0)

def up ( ) :
    t.setheading (90)

def down ( ) :
    t.setheading (270)
    
scr.onkey(left, "Left") # 키보드 입력 처리
scr.onkey(right, "Right")
scr.onkey (up, "Up")
scr.onkey (down, "Down")
scr.listen( )

jumsu = 0

while True : # 게임의 핵심인 무한 루프
    t.forward(1)
    if t.xcor( ) <= -300 or t.xcor( ) >= 300 :
        t.right(180)
    if t.ycor( ) <= -300 or t.ycor( ) >= 300 :
        t.right(180) # 밑에서부터 충돌처리
    if -10 < t.xcor( ) - food.xcor( ) < 10 and -10 < t.ycor( ) - food.ycor( ) < 10 :
        food.goto(random.randint(-300, 300), random.randint(-300, 300))
        jumsu = jumsu + 10
        t.write (jumsu)
