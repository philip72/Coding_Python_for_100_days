from turtle import Turtle, Screen
import time
from snake import Snake
import food
from scoreboard import Score

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
food= food.Food()
score=Score()

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

    #detect collosion with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    #detect collision with wall
        if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
            game_is_on=False
    
    #detect collison  with tail, if head collides with any segment  in the tail
            for segment in snake.segments[1:]:
                # if segment==snake.head:
                #     pass
                if snake.head.distance(segment)<10:
                    game_is_on=False
                    score.game_over()

    




screen.exitonclick()