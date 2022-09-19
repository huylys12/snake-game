from turtle import Turtle

FONT = ('Segue UI', 20, 'normal')
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt", mode="r") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        self.update()

    def reset_game(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()
