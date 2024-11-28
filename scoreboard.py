from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Initial Setup
        self.ht()
        self.color("white")
        self.font = ("Arial", 20, "normal")

    def update_scoreboard(self, score, high_score, lives):
        self.clear()
        self.teleport(290, 450)
        self.write(f"Score: {score}", font=("Arial", 20, "normal"))

        self.teleport(-400, 450)
        self.write(f"High Score: {high_score}", font=("Arial", 20, "normal"))

        self.teleport(-400, -450)
        self.write(f"Lives left: {lives}", font=("Arial", 20, "normal"))
