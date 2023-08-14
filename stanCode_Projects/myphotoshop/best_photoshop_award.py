"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.22
BLACK_PIXEL = 240


def main():
    """
    When I first time hear this homework, my first mind is that I want to be a part of a famous comic --
    Attack on Titan.
    So I decided to make a image that I scared the Titan and run away quickly.
    """
    fg = SimpleImage('image_contest/me2.png')
    bg = SimpleImage('image_contest/back.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(back, me):
    for y in range (back.height):
        for x in range(back.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.green = pixel_bg.green
                pixel_me.blue = pixel_bg.blue
    return me


if __name__ == '__main__':
    main()
