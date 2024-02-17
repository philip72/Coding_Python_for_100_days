from turtle import Turtle, Screen

timmy_the_turtle= Turtle()

timmy_the_turtle.shape('turtle')

# timmy_the_turtle.forward(100)

""" Drawing a square"""

import random
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

for i in range(50):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)

color= ['red', 'green']

def draw_shape(num_of_sides):
    angle= 360/num_of_sides

    for _ in num_of_sides:
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for i in range(3,11):
    timmy_the_turtle.color(random.choice(color))
    draw_shape(i)
    


screen= Screen()

screen.exitonclick()