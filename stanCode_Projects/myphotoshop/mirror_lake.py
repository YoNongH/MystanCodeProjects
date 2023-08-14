"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original colored image
    """
    original_mt = SimpleImage(filename)
    h_original_mt = SimpleImage.blank(original_mt.width, original_mt.height*2)
    for y in range(original_mt.height):
        for x in range(original_mt.width):
            p_colored = original_mt.get_pixel(x, y)
            p_b1 = h_original_mt.get_pixel(x, y)
            p_b2 = h_original_mt.get_pixel(x, h_original_mt.height-1-y)
            p_b1.red = p_colored.red
            p_b1.green = p_colored.green
            p_b1.blue = p_colored.blue
            p_b2.red = p_colored.red
            p_b2.green = p_colored.green
            p_b2.blue = p_colored.blue
    return h_original_mt


def main():
    """
    Make a image be like a upside down mirror picture.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
