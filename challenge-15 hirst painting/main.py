import random
import turtle as Turtile_module

tr = Turtile_module.Turtle()
sc = Turtile_module.Screen()

Turtile_module.colormode(255)

tr.speed('fastest')
tr.penup()


color_list = [(20, 247, 44), (208, 245, 246), (213, 154, 96), (52, 107, 32), (179, 177, 31), (202, 142, 31)]
def drawer():
    for i in range(10):
        tr.pendown()
        tr.dot(20,random.choice(color_list))
        tr.penup()
        tr.forward(40)
        tr.pendown()

for i in range(8):
    tr.setposition(0,50*i)
    drawer()
    tr.penup()


sc.exitonclick()