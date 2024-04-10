from turtle import Turtle, Screen
import random

sc = Screen()

sc.setup(700,500)

color = ['red','green','blue','black','pink','purple']
position = [-100,-50,0,50,100,150]
user_bet = sc.textinput(title='Make your Bet',prompt='Which turtile will win the race ? enter color')

all_turtle = []

for i in range(6):
    tr = Turtle()
    tr.shape('turtle')
    tr.color(color[i])
    tr.penup()
    tr.goto(x=-270,y=position[i])
    all_turtle.append(tr)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        random_move = random.randint(1,10)
        turtle.forward(random_move)
        if turtle.xcor()>270:
            is_race_on=False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print('you won')
            else:
                print(f'you lost, the winner is {turtle.pencolor()}')

sc.exitonclick()



