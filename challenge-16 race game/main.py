from turtle import Turtle, Screen

tr = Turtle()
sc = Screen()

sc.setup(700,500)

color = ['red','green','blue','black','pink','purple']
tr.shape('turtle')

for i in range(7):
    tr.color(color[i])
    tr.goto()

sc.exitonclick()