from turtle import Turtle, Screen
import paddle


screen=Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong Game')

screen.listen()
screen.onkey(.up, "Up")
screen.onkey(snake.down, "Down")
screen.exitonclick()