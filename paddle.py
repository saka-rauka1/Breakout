from turtle import Turtle

PADDLE_SPEED = 100
WIDTH_MULT = 0.5
LENGTH_MULT = 10


class Paddle(Turtle):
    def __init__(self, screen_dimensions):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(WIDTH_MULT, LENGTH_MULT) # 10x200

        # Assign attributes for use in collision detection
        self.length = LENGTH_MULT * 20 # 200
        self.height = WIDTH_MULT * 20 # 10

        # Define boundaries
        self.min_x = -screen_dimensions[0] / 2 + 100
        self.max_x = screen_dimensions[0] / 2 - 100
        self.min_y = -screen_dimensions[1] / 2 + 20

        self.teleport(0, self.min_y)

    def move_left(self):
        if self.xcor() > self.min_x:
            self.bk(PADDLE_SPEED)

    def move_right(self):
        if self.xcor() < self.max_x:
            self.fd(PADDLE_SPEED)
