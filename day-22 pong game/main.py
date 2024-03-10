# Import necessary modules
from turtle import Turtle, Screen
from paddle import Paddle
from pong_ball import PongBall
from scoreboard import Scoreboard
import time


screen=Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)

paddle_right= Paddle()
paddle_right.create_right_paddle()

# Listen for keyboard input
screen.listen()
screen.onkey(paddle_right.up, 'Up')
screen.onkey(paddle_right.down, 'Down')
game_on=True
while game_on:
    screen.update()

# Exit the game when the user clicks anywhere
screen.exitonclick()
