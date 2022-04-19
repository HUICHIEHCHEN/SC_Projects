"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program allows user to play Breakout game in a defined number of turns (NUM_LIVES).
Once user clicks, game starts, and once the game starts, user can use mouse to control the paddle
to hit the ball against the bricks and eliminate them.
If the paddle misses the ball, user will lose a turn.
When user loses all turns, user loses the game.
When all bricks are eliminated, user wins the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Animation loop
    while True:
        graphics.set_lives(lives)       # Record the number of remaining lives
        if graphics.execute:
            if lives > 0 and graphics.num_bricks > 0:
                graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                graphics.detect()
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                    graphics.set_dx(-1 * graphics.get_dx())
                elif graphics.ball.y <= 0:
                    graphics.set_dy(-1 * graphics.get_dy())
                elif graphics.ball.y + graphics.ball.height > graphics.window.height:
                    graphics.reset()        # Reset the game
                    lives -= 1
        pause(FRAME_RATE)
        if lives == 0 or graphics.num_bricks == 0:      # Game over or win
            graphics.set_lives(lives)
            graphics.end()
            break


if __name__ == '__main__':
    main()