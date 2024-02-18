import turtle as t
import random
import colorgram as cg

colors = cg.extract('sweet_pic.jpg', 30)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
rgb_colors=[]

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

tut= t.Turtle()



t.colormode(255)
tut.setheading(225)
tut.forward(300)
tut.setheading(0)

for _ in range(20):
    tut.dot(20, random.choice(rgb_colors))
    tut.forward(50)



def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    random_colors= (r, g , b)
    return random_colors

screen= t.Screen()
screen.exitonclick()

