from turtle import Turtle 

shapesize= (5,1,0)
UP=90
DOWN=270

class Paddle:
    def __init__(self) -> None:
            self.create_right_paddle()
            self.create_left_paddle()
    def create_right_paddle(self):
            paddle= Turtle()
            paddle.color('white')
            paddle.shape('square')
            paddle.shapesize(shapesize)
            paddle.penup()
            paddle.goto(x=350,y=0)
    def create_left_paddle():
          pass
    def move(self):
         pass
    def up(self):
        new_y= paddle.ycor()+20
        paddle.goto(paddle.xcor(),new_y)

    def down(self):
        new_y= paddle.ycor()-20
        paddle.goto(paddle.xcor(),new_y)