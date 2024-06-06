from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super(Score_board, self).__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score:{self.score}')
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over")
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()