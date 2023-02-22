from turtle import Turtle

SCORE_ALIGN = "center"
SCORE_FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(arg=self.l_score, align=SCORE_ALIGN, font=SCORE_FONT)
        self.goto(100, 190)
        self.write(arg=self.r_score, align=SCORE_ALIGN, font=SCORE_FONT)

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
