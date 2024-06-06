from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.3,stretch_len=0.5)
        self.color('blue')
        self.speed('fastes')
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
