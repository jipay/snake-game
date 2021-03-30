from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, "center", 24)

    def add(self, value):
        self.score += value
        self.clear()
        self.write(f"Score: {self.score}", False, "center", 24)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over.\nfinal score: {self.score}", False, "center", 24)