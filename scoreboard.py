from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.score} ", align="Center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=("Arial", 20, "normal"))

    def sum_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score} ", align="Center", font=("Arial", 20, "normal"))