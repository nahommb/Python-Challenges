from turtle import Turtle, Screen


sc = Screen()

sc.setup(700,500)

color = ['red','green','blue','black','pink','purple']
position = [-100,-50,0,50,100,150]


for i in range(6):
    tr = Turtle()
    tr.shape('turtle')
    tr.color(color[i])
    tr.penup()
    tr.goto(x=-270,y=position[i])

sc.exitonclick()