"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: Spaceship
    :param figure_img: A woman with green screen
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            p_fig = figure_img.get_pixel(x, y)
            bigger = max(p_fig.red, p_fig.blue)
            if p_fig.green > bigger*2:
                p_back = background_img.get_pixel(x, y)
                p_fig.red = p_back.red
                p_fig.green = p_back.green
                p_fig.blue = p_back.blue
    return figure_img


def main():
    """
    Let two images combined by green screen.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
