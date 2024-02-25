from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Xenzie")
screen.tracer(0)

segment_1=Turtle('square')
segment_1.color('white')

segment_2=Turtle('square')
segment_2.color('white')
segment_2.goto(x=-20,y=0)


segment_3=Turtle('square')
segment_3.color('white')
segment_3.goto(x=-40,y=0)

#check on a for loop on how to create the three turtles

snake= Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")




game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

    snake.move()

    




screen.exitonclick()