from turtle import Turtle , Screen

tr = Turtle()
sc = Screen()
ty = Turtle()

sc.bgcolor('black')
sc.title("Snake Game")

sc.setup(700,700)

tr.shape('square')
tr.color('white')

ty.goto(-20,0)
ty.shape('square')
ty.color('white')


sc.exitonclick()
