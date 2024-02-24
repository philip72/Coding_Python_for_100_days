import turtle as turtle_module
import random
import colorgram as cg  


# Extract colors from 'sweet_pic.jpg' image using colorgram library
colors = cg.extract('image.jpg', 30)

# Initialize an empty list to store RGB colors extracted from the image
rgb_colors = []

# Extract RGB colors from Color objects returned by colorgram.extract
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

turtle_module.colormode(255)
tim= turtle_module.Turtle()

tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots= 100

for _ in range(1, number_of_dots+1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    if _ % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen= turtle_module.Screen()

screen.exitonclick()

