from turtle import Turtle 

UP=90
DOWN=270
paddle_right=Turtle()
paddle_right.color('white')
paddle_right.shape('rectangle')
paddle_right.shapesize(stretch_wid=20,stretch_len=100)
paddle_right.goto(x=350,y=0)

def up(self):
        if set.head.heading() != DOWN:
            self.head.setheading(UP)
def down(self):
        if set.head.heading() != UP:
            self.head.setheading(DOWN)


class Paddle:
      def __init__(self) -> None:
            self.create_paddle()
      def create_paddle(self):
            padd