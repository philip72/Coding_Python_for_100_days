from turtle import Turtle, Screen
from paddle import Paddle
from pong_ball import PongBall
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)
score_board= Scoreboard()
right_paddle = Paddle(350, 0)  # Initialize with starting coordinates
left_paddle = Paddle(-350, 0)  # Initialize with starting coordinates

pong_ball=PongBall()

screen.listen()
# Move right paddle
screen.onkey(right_paddle.go_up,'Up')
screen.onkey(right_paddle.go_down,'Down')

# Move left paddle
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    pong_ball.move_ball()

    #detect collision with wall
    #past the 300 or -300 then its too far up then its a collision

    if pong_ball.ycor() > 300 or pong_ball.ycor()<-300:
        #needs to bounce
        pong_ball.bounce_y()
    
    #dfetect collison with right_paddle
    if pong_ball.distance(right_paddle)<50 and pong_ball.xcor()>320 or pong_ball.distance(left_paddle)<50 and pong_ball.xcor()<-320:
        pong_ball.bounce_x()

    #when r missed
    if pong_ball.xcor()>380:
        pong_ball.reset_position()
        score_board.l_point()
    #when l missed
    if pong_ball.xcor()<-380:
        pong_ball.reset_position()
        score_board.r_point()

screen.exitonclick()
