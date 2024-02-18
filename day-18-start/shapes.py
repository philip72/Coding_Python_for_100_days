from turtle import Turtle, Screen

import random

tim= Turtle()

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "cyan",
    "magenta",
    "turquoise",
    "lavender",
    "maroon",
    "teal",
    "olive",
    "coral",
    "navy",
    "silver",
    "gold",
    "beige"
]
def draw_shape(no_of_sides):
    angle= 360/no_of_sides

    for _ in no_of_sides:
        tim.forward(100)
        tim.right(angle)

for every_shape in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(every_shape)

screen = Screen()
screen.exitonclick()