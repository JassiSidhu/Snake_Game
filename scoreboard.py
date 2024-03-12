from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as highscore:
                highscore.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
