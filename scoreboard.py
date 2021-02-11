from turtle import Turtle


<<<<<<< HEAD
=======

>>>>>>> 0530d7b... Initial commit
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
<<<<<<< HEAD
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.score} ", align="Center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=("Arial", 20, "normal"))
=======
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="Center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = -1
        self.sum_score()
>>>>>>> 0530d7b... Initial commit

    def sum_score(self):
        self.clear()
        self.score += 1
<<<<<<< HEAD
        self.write(f"Score : {self.score} ", align="Center", font=("Arial", 20, "normal"))
=======
        self.write(f"Score : {self.score}  High Score: {self.high_score}", align="Center", font=("Arial", 20, "normal"))
>>>>>>> 0530d7b... Initial commit
