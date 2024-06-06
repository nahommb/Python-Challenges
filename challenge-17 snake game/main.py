from turtle import Turtle , Screen
import time
from snake import Snake
from food import Food
from score_board import Score_board

tr = Turtle()
sc = Screen()
ty = Turtle()

sc.bgcolor('black')
sc.title("Snake Game")

sc.setup(700,700)
sc.tracer(0)

snake = Snake()
fd = Food()
score_board = Score_board()
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

    if snake.head.distance(fd)<15:
        print('eaten')
        fd.refresh()
        score_board.increase_score()
    if snake.head.xcor()>340 or snake.head.xcor()<-340 or snake.head.ycor()>340 or snake.head.ycor()<-340:
        score_board.game_over()
        game_is_on = False

sc.exitonclick()
