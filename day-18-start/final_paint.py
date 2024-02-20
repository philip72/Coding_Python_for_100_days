import turtle as t
import random
import colorgram as cg

# Extract colors from 'sweet_pic.jpg' image using colorgram library
colors = cg.extract('sweet_pic.jpg', 30)

# Initialize an empty list to store RGB colors extracted from the image
rgb_colors = []

# Extract RGB colors from Color objects returned by colorgram.extract
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# Initialize a Turtle object and set its speed
tut = t.Turtle()
tut.speed(9)

# Set color mode to 255 to use RGB color values
t.colormode(255)

# Set the initial heading and position of the turtle
tut.setheading(225)
tut.forward(300)
tut.setheading(0)

# Draw dots with random colors selected from the extracted RGB colors
for _ in range(20):
    tut.dot(20, random.choice(rgb_colors))
    tut.forward(50)

# Define a function to generate random RGB colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

# Create a screen for the turtle graphics and exit on click
screen = t.Screen()
screen.exitonclick()
