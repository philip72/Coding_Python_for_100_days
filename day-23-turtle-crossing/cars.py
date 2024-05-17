from turtle import Turtle

class Cars(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('rectangle')
    self.color('white')
  def colors(self):
    self.list_of_colors=[]
    
