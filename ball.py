from turtle import Turtle
from random import randint

BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self, screen_dimensions):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")

        # Assign attributes for use in collision detection
        self.length = 20
        self.height = 20

        # Define boundaries
        self.min_x = -screen_dimensions[0] / 2 + 10
        self.max_x = screen_dimensions[0] / 2 - 10
        self.min_y = -screen_dimensions[1] / 2 + 10
        self.max_y = screen_dimensions[1] / 2 - 10

        self.spawn_ball()

    def spawn_ball(self):
        self.teleport(0, self.min_y + 30)
        self.setheading(randint(30, 150))

    def move_ball(self):
        self.fd(BALL_SPEED)
