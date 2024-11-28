from turtle import Screen
from block_manager import BlockManager
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

SCREEN_DIMENSIONS = (960, 1000)
SCORE = 0
HIGH_SCORE = 0
MAX_LIVES = 3
LIVES_LEFT = MAX_LIVES

if __name__ == '__main__':
    # Create the screen
    screen = Screen()
    screen.title("Breakout")
    screen.setup(*SCREEN_DIMENSIONS)
    screen.bgcolor("black")
    screen.listen()
    screen.tracer(0) # Disable animations until setup is complete

    # Create the scoreboard
    scoreboard = Scoreboard()
    with open("high_score.txt") as file:
        HIGH_SCORE = int(file.read())
    scoreboard.update_scoreboard(SCORE, HIGH_SCORE, LIVES_LEFT)

    # Create rows of blocks
    block_manager = BlockManager()

    # Create ball
    ball = Ball(SCREEN_DIMENSIONS)

    # Create and move the paddle
    paddle = Paddle(SCREEN_DIMENSIONS)
    screen.onkey(fun=paddle.move_left, key="Left")
    screen.onkey(fun=paddle.move_right, key="Right")

    screen.tracer(1) # Re-enable animations now that setup is complete

    # Game loop
    game_is_running = True
    while game_is_running:
        ball.move_ball()

        # Handle collisions with blocks
        block_collision_distance_height = abs(ball.height / 2 - block_manager.block_height / 2)
        block_collision_distance_width = abs(ball.length / 2 - block_manager.block_length / 2)

        for block in block_manager.blocks:
            if abs(ball.ycor() - block.ycor()) <= block_collision_distance_height:
                if abs(ball.xcor() - block.xcor()) <= block_collision_distance_width:
                    # Handle Scoring
                    match block.fillcolor():
                        case "Yellow":
                            SCORE += 1
                        case "Green":
                            SCORE += 2
                        case "Orange":
                            SCORE += 3
                        case "Red":
                            SCORE += 4
                        case _:
                            pass
                    screen.tracer(0) # Disable tracer to avoid noticeable lag when redrawing scoreboard
                    scoreboard.update_scoreboard(SCORE, HIGH_SCORE, LIVES_LEFT)
                    screen.tracer(1) # Re-enable tracer

                    # Handle ball rebounding
                    if ball.ycor() > block.ycor(): # Top of block
                        ball.setheading(360 - ball.heading())
                    elif ball.ycor() < block.ycor(): # Bottom of block
                        ball.setheading(0 - ball.heading())
                    elif ball.xcor() < block.xcor(): # Left of block
                        ball.setheading(180 - ball.heading())
                    elif ball.xcor() > block.xcor(): # Right of block
                        ball.setheading(540 - ball.heading())

                    block.reset() # Remove the block

                    # End game if there are no more blocks
                    if len(block_manager.blocks) == 0:
                        game_is_running = False
                        if SCORE > HIGH_SCORE:
                            with open("high_score.txt", mode="w") as file:
                                file.write(str(SCORE))

        # Handle collisions with walls
        if ball.xcor() > ball.max_x:
            ball.setheading(180 - ball.heading())
        if ball.xcor() < ball.min_x:
            ball.setheading(540 - ball.heading())
        if ball.ycor() > ball.max_y:
            ball.setheading(0 - ball.heading())
        if ball.ycor() < ball.min_y:
            LIVES_LEFT -= 1
            screen.tracer(0) # Disable tracer to avoid noticeable lag when redrawing scoreboard
            scoreboard.update_scoreboard(SCORE, HIGH_SCORE, LIVES_LEFT)
            screen.tracer(1) # Re-enable tracer
            if LIVES_LEFT > 0:
                ball.spawn_ball()
            else:
                game_is_running = False
                if SCORE > HIGH_SCORE:
                    with open("high_score.txt", mode="w") as file:
                        file.write(str(SCORE))

        # Handle collisions with paddle
        # todo Bug where the ball collides with a wall near to the paddle
        paddle_collision_distance_height = abs(ball.height / 2 - paddle.height / 2)
        paddle_collision_distance_width = abs(ball.length / 2 - paddle.length / 2)

        if abs(ball.ycor() - paddle.ycor()) <= paddle_collision_distance_height:
            if abs(ball.xcor() - paddle.xcor()) <= ball.length + 10: # Hits near the centre
                ball.setheading(360 - ball.heading())
            elif abs(ball.xcor() - paddle.xcor()) <= paddle_collision_distance_width:
                if ball.xcor() < paddle.xcor(): # Hits left side
                    ball.setheading(360 - ball.heading() + 20)
                else: # Hits right side
                    ball.setheading(360 - ball.heading() - 20)


    screen.mainloop()

    # todo Move screen tracer stuff into scoreboard module rather than repeatedly turning it off and on here
    # todo Proper game over screen
    # todo Rebound code is very basic and should be improved
