"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The Animation code encode the Breakout Project from Noah Huang.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        if lives == 0 or graphics.total_brick == 0:
            break
        else:
            if graphics.start != 0:
                graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    graphics.set_dx()
                if graphics.ball.y <= 0:
                    graphics.set_dy()
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    lives -= 1
                    graphics.reset_ball()
            if graphics.get_dx() != 0 or graphics.get_dy() != 0:   # Ball won't affect the block at first
                graphics.ball_get_obj()
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
