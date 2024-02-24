import turtle as tut_module 
import random

#state
#timmy.color= green
#timmy.color= purple
screen= tut_module.Screen()
screen.setup(width=500,height=400)

is_race_on= False

colors=["red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"] 
y_pos= [-70, -40, -10, 20, 50, 80]
all_turtle=[]

for turtle_index  in range(0,7):
    tut= tut_module.Turtle(shape='turtle')
    tut.color(colors[turtle_index])
    tut.penup()
    tut.goto(x=-230, y=y_pos[turtle_index])
    all_turtle.append(tut)


user_bet= screen.textinput(title='Make your bet', prompt='Which turtle will win the race? enter color')
#arrange them on how they win
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor>230:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color==user_bet:
                print('you win')
            else:
                print('you lost')
        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()


# create a list and eploy different names for the turtles
#expanding