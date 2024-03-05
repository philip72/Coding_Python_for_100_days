from turtle import Turtle, Screen
from paddle import Paddle


screen=Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong Game')
screen.tracer(0)

paddle_right= Paddle()
paddle_right.create_right_paddle()

screen.listen()
screen.onkey(paddle_right.up, 'Up')
screen.onkey(paddle_right.down, 'Down')
game_on=True
while game_on:
    screen.update()

screen.exitonclick()