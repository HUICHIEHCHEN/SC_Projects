"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program sets up the settings for Breakout game.
The game settings include the size of window, brick, ball, and paddle,
as well as the velocity for the ball and mouse control of paddle.
Once the user clicks and starts the game, the switch for mouse click will be turned off.
During the game, user can only move the mouse to control the paddle.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)//2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball_start_x = (window_width-self.ball.width)//2
        self.ball_start_y = (window_height-self.ball.height)//2
        self.window.add(self.ball, x=self.ball_start_x, y=self.ball_start_y)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        self.execute = False
        onmouseclicked(self.start_ball)

        # Record the number of lives
        self.lives = 0

        # Create labels for game wins and loses
        self.lose = GLabel('GAME OVER!')
        self.lose.font = '-30'
        self.win = GLabel('Congrats!')
        self.win.font = '-30'

        # Draw bricks and record the total number of bricks
        self.num_bricks = brick_rows * brick_cols
        self.brick_color = 'black'
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i % 2 == 0:
                    self.brick_color = self.set_color(i)
                else:
                    self.brick.fill_color = self.brick_color
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=brick_offset + i * (brick_height + brick_spacing))

    # Fill bricks with given colors
    def set_color(self, i):
        if i > 8:
            i = (i % 10)
        if i == 0:
            self.brick.fill_color = 'red'
        elif i == 2:
            self.brick.fill_color = 'orange'
        elif i == 4:
            self.brick.fill_color = 'yellow'
        elif i == 6:
            self.brick.fill_color = 'green'
        elif i == 8:
            self.brick.fill_color = 'blue'
        return self.brick.fill_color

    # Enable the mouse to control the paddle
    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width

    # Enable mouse click to start the game and set the velocity for the ball
    def start_ball(self, mouse):
        if not self.execute:
            if self.lives > 0 and self.num_bricks > 0:
                self.execute = True     # Close the mouse click
                self.__dy = INITIAL_Y_SPEED
                self.__dx = random.randint(1, MAX_X_SPEED)
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    # Record the number of remaining lives
    def set_lives(self, lives):
        self.lives = lives

    # Determine whether the ball hits the paddle or bricks
    def detect(self):
        for x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                detect_object = self.window.get_object_at(x, y)
                if detect_object is not None:
                    if detect_object is not self.paddle:        # The ball hits bricks
                        self.window.remove(detect_object)       # Remove the brick hit by the ball
                        self.__dy = -self.__dy
                        self.num_bricks -= 1
                        return
                    elif detect_object is self.paddle and self.__dy > 0:    # The ball hits the paddle
                        self.__dy = -self.__dy

    # Allow the user to get the velocity of the ball
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    # Reset game and put the ball back to the starting position
    def reset(self):
        self.window.add(self.ball, x=self.ball_start_x, y=self.ball_start_y)
        self.execute = False        # Allow mouse click to execute the game

    # Display the screen of win/lose
    def end(self):
        self.window.clear()
        if self.lives == 0:
            self.window.add(self.lose, x=(self.window.width - self.lose.width) // 2,
                            y=(self.window.height - self.lose.height) // 2)
        elif self.num_bricks == 0:
            self.window.add(self.win, x=(self.window.width - self.win.width) // 2,
                            y=(self.window.height - self.win.height) // 2)
