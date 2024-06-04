from turtle import Turtle , Screen
import time
from snake import Snake

tr = Turtle()
sc = Screen()
ty = Turtle()

sc.bgcolor('black')
sc.title("Snake Game")

sc.setup(700,700)
sc.tracer(0)
snake = Snake()

game_is_on = True

sc.listen()
sc.onkey(snake.up,'Up')
sc.onkey(snake.down,'Down')
sc.onkey(snake.left,'Left')
sc.onkey(snake.right,'Right')



while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()


sc.exitonclick()
