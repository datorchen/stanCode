"""
File: breakoutgraphics.py
Name: Sean Chen
---------------------------
Provide a :class:'BreakoutGraphics' to support the creation of a Breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
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
        self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT,
                            x=(self.window.width-PADDLE_WIDTH)/2, y=(self.window.height-PADDLE_OFFSET))
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2,
                          x=self.window.width/2-BALL_RADIUS, y=self.window.height/2-BALL_RADIUS)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT,
                              x=j*(BRICK_WIDTH+BRICK_SPACING), y=i*(BRICK_HEIGHT+BRICK_SPACING))
                self.brick.filled = True

                # Set color of bricks with the order of rainbow color for every two rows
                if 0 <= i % 14 <= 1:
                    self.brick.fill_color = 'red'
                elif 2 <= i % 14 <= 3:
                    self.brick.fill_color = 'orange'
                elif 4 <= i % 14 <= 5:
                    self.brick.fill_color = 'yellow'
                elif 6 <= i % 14 <= 7:
                    self.brick.fill_color = 'green'
                elif 8 <= i % 14 <= 9:
                    self.brick.fill_color = 'blue'
                elif 10 <= i % 14 <= 11:
                    self.brick.fill_color = 'indigo'
                else:
                    self.brick.fill_color = 'purple'
                self.window.add(self.brick)

    def paddle_move(self, mouse):
        """
        Move the paddle horizontally with mouse.
        :param mouse: mouse event when mouse move
        """
        if 0 + self.paddle.width / 2 <= mouse.x <= self.window.width - self.paddle.width / 2:
            self.paddle.x = mouse.x - self.paddle.width / 2
        elif mouse.x < 0 + self.paddle.width / 2:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width - self.paddle.width

    def set_ball_velocity(self, mouse):
        """
        Set moving speed of the ball.
        :param mouse: mouse event when mouse clicked
        """
        if self.__dx == self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx *= -1

    def get_dxdy(self):
        """
        Get the set moving speed of the ball.
        :return: horizontal and vertical moving speed
        """
        dx = self.__dx
        dy = self.__dy
        self.__dx = 0
        self.__dy = 0
        return dx, dy

    def get_brick_rows_and_cols(self):
        """
        Get value of constants 'BRICK_ROWS' and 'BRICK_COLS'.
        :return: constants 'BRICK_ROWS' and 'BRICK_COLS'
        """
        brick_rows = BRICK_ROWS
        brick_cols = BRICK_COLS
        return brick_rows, brick_cols

    def remove_all_objs(self):
        # Remove all objects except window in a BreakoutGraphics object.
        self.window.remove(self.paddle)
        self.window.remove(self.ball)
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                obj = self.window.get_object_at(x=j*(BRICK_WIDTH+BRICK_SPACING), y=i*(BRICK_HEIGHT+BRICK_SPACING))
                if obj:
                    self.window.remove(obj)

    def game_over(self):
        # Show 'GAME OVER :(' when a game is over.
        label = GLabel('GAME OVER :(')
        label.font = '-35'
        self.window.add(label, x=(self.window.width-label.width)/2, y=(self.window.height-label.height)/2)

    def win(self):
        # Show 'YOU WIN :)' when a player removes all the bricks.
        label = GLabel('YOU WIN :)')
        label.font = '-35'
        self.window.add(label, x=(self.window.width-label.width)/2, y=(self.window.height-label.height)/2)

    def brick_exist_checking(self):
        """
        Check if there is any bricks in a BreakoutGraphics object.
        :return: 'True' if there is any bricks in a BreakoutGraphics object; 'False' if there is none.
        """
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                obj = self.window.get_object_at(x=j*(BRICK_WIDTH+BRICK_SPACING), y=i*(BRICK_HEIGHT+BRICK_SPACING))
                if obj:
                    return True
        return False