# Cauldron
from turtle import *
t = Turtle()
t.speed(80)
t.pensize(5)

# Position the turtle to start cauldron
t.penup()
t.setpos(-80,-120)

# Draw oval of cauldron
t.pendown()
t.seth(-45)
t.color("black")
t.fillcolor("black")
t.begin_fill()
t.circle(110,90)
t.circle(80,90)
t.circle(110,90)
t.circle(80,90)
t.end_fill()

# Draw left foot of cauldron
t.penup()
t.setpos(-50,-140)
t.pensize(30)
t.right(50)
t.pendown()
t.forward(20)

# Draw right foot of cauldron
t.penup()
t.setpos(45,-140)
t.left(8)
t.pendown()
t.forward(20)

# Draw lip
t.penup()
t.setpos(-90,13)
t.left(87)
t.pendown()
t.forward(174)

# Draw highlight for cauldron
t.penup()
t.color("white")
t.setpos(-54,-3)
t.pendown()
t.pensize(5)
t.forward (70)

# Draw small bubble
t.penup()
t.setpos(-10,50)
t.pendown()
t.pensize(3)
t.color("black")
t.circle(15)
t.penup()
t.setpos(-10,74)
t.left(180)
t.pensize(2)
t.pendown()
t.circle(10,90)

# Draw middle bubble
t.penup()
t.setpos(10,100)
t.pendown()
t.pensize(4)
t.color("black")
t.circle(20)
t.penup()
t.setpos(30,114)
t.right(90)
t.pensize(2.5)
t.pendown()
t.circle(14,90)

# Draw big bubble
t.penup()
t.setpos(-45,150)
t.pendown()
t.pensize(4.5)
t.color("black")
t.circle(30)
t.penup()
t.setpos(-20,170)
t.right(80)
t.pensize(3)
t.pendown()
t.circle(20,90)
t.penup()
t.setpos(0,-400)

