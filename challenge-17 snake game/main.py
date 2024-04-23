from turtle import Turtle , Screen
import time

tr = Turtle()
sc = Screen()
ty = Turtle()

sc.bgcolor('black')
sc.title("Snake Game")

sc.setup(700,700)
sc.tracer(0)
starting_position = [(0,0),(-20,0),(-40,0)]

segment =[]

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segment.append(new_segment)

game_is_on = True

while game_is_on:
    sc.update()
    time.sleep(0.1)
    for seg in range(len(segment)-1,0,-1):
        new_x = segment[seg-1].xcor()
        new_y = segment[seg-1].ycor()
        segment[seg].goto(new_x,new_y)
    segment[0].forward(20)
    segment[0].left(90)



sc.exitonclick()
