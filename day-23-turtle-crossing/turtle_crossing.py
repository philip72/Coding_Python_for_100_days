from turtle import Turtle

class TurtleCrossing(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()
    
    def create_turtle(self):
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.goto(0,-300)
    
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)