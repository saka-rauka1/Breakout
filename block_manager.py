from turtle import Turtle

WIDTH_MULT = 2.5
LENGTH_MULT = 5


class BlockManager:
    def __init__(self):
        self.blocks = []
        self.create_rows()

        # Assign attributes for use in collision detection
        self.block_length = LENGTH_MULT * 20 # 100
        self.block_height = WIDTH_MULT * 20 # 50

    def create_block(self, color, pos):
        block = Turtle()
        block.shape("square")
        block.color(color)
        block.shapesize(WIDTH_MULT, LENGTH_MULT) # 50x100
        block.teleport(*pos)
        self.blocks.append(block)

    def create_rows(self):
        for y in range(4):
            for x in range(8):
                match y:  # Switch color from yellow through to red from the bottom row to the top
                    case 0:
                        color = "Yellow"
                    case 1:
                        color = "Green"
                    case 2:
                        color = "Orange"
                    case 3:
                        color = "Red"
                    case _:
                        color = "White"

                pos = -420 + x * 120, 125 + y * 60 # 100x50 blocks with 20 units of gap l-r and 10 t-b
                self.create_block(color, pos)
