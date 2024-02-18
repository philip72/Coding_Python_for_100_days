import turtle as t
import random

t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    random_colors= (r, g , b)
    return random_colors
tut=t.Turtle()
# tut.circle(50)
# tut.position()
# no_of_rotation= range(200)
# angle=360/no_of_rotation

# for _ in no_of_rotation:
#     tut.color(random_color)
#     tut.circle(50)
#     tut.position()
#     tut.right(angle)

def draw_spiral(no_of_gap):
    for _ in range(int(360/no_of_gap)):
        tut.color(random_color)
        tut.circle(100)
        tut.setheading(tut.heading()+no_of_gap)

draw_spiral(5)
        

screen=t.Screen()
screen.exitonclick()