from turtle import Turtle , Screen

tr = Turtle()
sc = Screen()
ty = Turtle()

sc.bgcolor('black')
sc.title("Snake Game")

sc.setup(700,700)

starting_position = [(0,0),(-20,0),(-40,0)]

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(position)


sc.exitonclick()
