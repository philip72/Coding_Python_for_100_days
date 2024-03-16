from turtle import Turtle, Screen

screen= Screen()
screen.bgcolor('black')
turtle1=Turtle(shape='square')

turtle1.color('yellow')

turtle1.penup()
screen.tracer(0)

game_on=True

while game_on:
    screen.update()
    turtle1.goto(0,-330)



screen.exitonclick()