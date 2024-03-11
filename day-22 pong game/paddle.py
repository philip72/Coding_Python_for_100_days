from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)#here it takes tuples

    def create_paddle(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate
        #we got rid of creating a new Turtle cause already the class carries the Turtle class
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_coordinate, y_coordinate)
        

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
