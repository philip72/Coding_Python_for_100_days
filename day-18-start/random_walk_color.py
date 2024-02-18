import turtle as t

import random 

tut_col= t.Turtle()
t.colormode(255)


def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    random_colors= (r, g , b)
    return random_colors

directions= [0,90,180,270]
tut_col.speed('fast')
tut_col.pensize(15)

def random_walks():
    tut_col.color(random_color())
    tut_col.forward(30)
    tut_col.setheading(random.choice(directions))

for _ in range(200):
    random_walks()

