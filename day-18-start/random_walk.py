import random
from turtle import Turtle, Screen

tut = Turtle()
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
direction= [tut.left(),tut.right(), tut.forward(), tut.back() ]

for _ in direction:
    tut.speed(9)
    random.choice(direction)

directions= [0,90,180,270]
tut.speed(9)
tut.width(15)
for _ in range(300):
    tut.color(random.choice(colors))
    tut.forward(30)
    tut.setheading(random.choice(directions))

screen= Screen()
screen.exitonclick()