from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, "center", 24)

    def update(self):
        # self.score += value
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game Over.\nfinal score: {self.score}", False, "center", 24)

    def get_high_score(self):
        with open("high_score.txt", mode="r") as file:
            return int(file.read())

    def set_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
