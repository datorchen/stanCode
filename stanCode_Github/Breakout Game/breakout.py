"""
File: breakout.py
Name: Sean Chen
---------------------------
This program creates a Breakout game.
Players use mouse to control a paddle to bounce a moving ball.
Bricks would be removed once hit by a ball.
Players win the game by removing all the bricks.
Players loss the game when NUM_LIVES is reduced to zero.
NUM_LIVES would be reduced by one when the ball drops under the paddle.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # Create a Breakout game.
    graphics = BreakoutGraphics()
    dx = 0
    dy = 0
    obj_last = 0
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if dx == dy == 0:
            dx, dy = graphics.get_dxdy()
        graphics.ball.move(dx, dy)
        if not 0 <= graphics.ball.x <= graphics.window.width - graphics.ball.width:
            dx *= -1
        if not 0 <= graphics.ball.y:
            dy *= -1

        vertex_list = [(graphics.ball.x, graphics.ball.y), (graphics.ball.x+graphics.ball.width, graphics.ball.y),
                       (graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height),
                       (graphics.ball.x, graphics.ball.y+graphics.ball.height)]
        for vertex in vertex_list:
            x = vertex[0]
            y = vertex[1]
            obj = graphics.window.get_object_at(x, y)
            if obj and obj is obj_last:
                break
            if obj and obj is not graphics.paddle:
                dy *= -1
                graphics.window.remove(obj)
                break
            if obj is graphics.paddle:
                dy *= -1
                break
        if obj:
            obj_last = obj

        # Reduce one life when the ball drop under the paddle.
        if graphics.ball.y > graphics.window.height:
            dx = dy = 0
            graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
            graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2
            lives -= 1

        # Check game-over condition.
        if lives == 0:
            graphics.remove_all_objs()
            graphics.game_over()
            break

        # Check winning condition.
        if not graphics.brick_exist_checking():
            graphics.remove_all_objs()
            graphics.win()
            break

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
