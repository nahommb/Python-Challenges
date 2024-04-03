import colorgram
from turtle import Turtle , Screen

tr = Turtle()
sc = Screen()

tr.speed('fastest')
tr.penup()
tr.goto(-40,0)

colors = colorgram.extract('image.jpg',6)
all_colors = []

for individual_color in colors:
    r = individual_color.rgb.r
    g = individual_color.rgb.g
    b = individual_color.rgb.b
    all_colors.append((r,g,b))


print(all_colors)
color_list = [[(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31)]]
def drawer():
    for i in range(10):
        tr.pendown()
        tr.circle(10)
        tr.penup()
        tr.forward(40)
        tr.pendown()

for i in range(8):
    tr.pendown()
    drawer()
    tr.penup()
    tr.setposition(0,50*i)

sc.exitonclick()