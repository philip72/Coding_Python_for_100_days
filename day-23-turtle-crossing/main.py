from turtle import Turtle, Screen
from turtle_crossing import TurtleCrossing

screen= Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.setup(width=800, height=600)
screen.title('Turtle Crossing Road')
screen.tracer(0)

turtle_crossing= TurtleCrossing()
screen.listen()
screen.onkey(turtle_crossing.go_up, 'Up')


game_on=True

while game_on:
    screen.update()



screen.exitonclick()