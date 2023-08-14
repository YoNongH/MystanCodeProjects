"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    old_img = SimpleImage("images/smiley-face.png")
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            p_new_img = new_img.get_pixel(x, y)
            if x == 0 and y == 0:
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x+1, y)
                s3 = old_img.get_pixel(x, y+1)
                s4 = old_img.get_pixel(x+1, y+1)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red) // 4
                p_new_img.green = (s1.green + s2.green + s3.green + s4.green) // 4
                p_new_img.blue = (s1.blue + s2.blue + s3.blue + s4.blue) // 4
            elif x == (old_img.width-1) and y == 0:
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x-1, y)
                s3 = old_img.get_pixel(x-1, y+1)
                s4 = old_img.get_pixel(x, y+1)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red) // 4
                p_new_img.green = (s1.green + s2.green + s3.green + s4.green) // 4
                p_new_img.blue = (s1.blue + s2.blue + s3.blue + s4.blue) // 4
            elif x == 0 and y == (old_img.height-1):
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x+1, y)
                s3 = old_img.get_pixel(x, y-1)
                s4 = old_img.get_pixel(x+1, y-1)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red) // 4
                p_new_img.green = (s1.green + s2.green + s3.green + s4.green) // 4
                p_new_img.blue = (s1.blue + s2.blue + s3.blue + s4.blue) // 4
            elif x == (old_img.width-1) and y == (old_img.height-1):
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x-1, y)
                s3 = old_img.get_pixel(x-1, y-1)
                s4 = old_img.get_pixel(x, y-1)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red) // 4
                p_new_img.green = (s1.green + s2.green + s3.green + s4.green) // 4
                p_new_img.blue = (s1.blue + s2.blue + s3.blue + s4.blue) // 4
            elif y == 0 and x != 0 and x != (old_img.width-1):
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x-1, y)
                s3 = old_img.get_pixel(x-1, y+1)
                s4 = old_img.get_pixel(x, y+1)
                s5 = old_img.get_pixel(x+1, y+1)
                s6 = old_img.get_pixel(x+1, y)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red + s5.red + s6.red) // 6
                p_new_img.green = (s1.green + s2.green + s3.green + s4.green + s5.green + s6.green) // 6
                p_new_img.blue = (s1.blue + s2.blue + s3.blue + s4.blue + s5.blue + s6.blue) // 6
            elif y == (old_img.height-1) and x != 0 and x != (old_img.width-1):
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x-1, y)
                s3 = old_img.get_pixel(x-1, y-1)
                s4 = old_img.get_pixel(x, y-1)
                s5 = old_img.get_pixel(x+1, y-1)
                s6 = old_img.get_pixel(x+1, y)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red + s5.red + s6.red) // 6
                p_new_img.green = (s1.green + s2.green + s3.green + s4.green + s5.green + s6.green) // 6
                p_new_img.blue = (s1.blue + s2.blue + s3.blue + s4.blue + s5.blue + s6.blue) // 6
            elif x == 0 and y != (old_img.height-1) and y != 0:
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x, y-1)
                s3 = old_img.get_pixel(x+1, y-1)
                s4 = old_img.get_pixel(x+1, y)
                s5 = old_img.get_pixel(x+1, y+1)
                s6 = old_img.get_pixel(x, y+1)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red + s5.red + s6.red) // 6
                p_new_img.green = (s1.green + s2.green + s3.green + s4.green + s5.green + s6.green) // 6
                p_new_img.blue = (s1.blue + s2.blue + s3.blue + s4.blue + s5.blue + s6.blue) // 6
            elif x == (old_img.width-1) and y != (old_img.height-1) and y != 0:
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x, y-1)
                s3 = old_img.get_pixel(x-1, y-1)
                s4 = old_img.get_pixel(x-1, y)
                s5 = old_img.get_pixel(x-1, y+1)
                s6 = old_img.get_pixel(x, y+1)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red + s5.red + s6.red) // 6
                p_new_img.green = (s1.green + s2.green + s3.green + s4.green + s5.green + s6.green) // 6
                p_new_img.blue = (s1.blue + s2.blue + s3.blue + s4.blue + s5.blue + s6.blue) // 6
            else:
                s1 = old_img.get_pixel(x, y)
                s2 = old_img.get_pixel(x, y+1)
                s3 = old_img.get_pixel(x, y-1)
                s4 = old_img.get_pixel(x+1, y)
                s5 = old_img.get_pixel(x+1, y+1)
                s6 = old_img.get_pixel(x+1, y-1)
                s7 = old_img.get_pixel(x-1, y)
                s8 = old_img.get_pixel(x-1, y+1)
                s9 = old_img.get_pixel(x-1, y-1)
                p_new_img.red = (s1.red + s2.red + s3.red + s4.red + s5.red + s6.red + s7.red + s8.red + s9.red) // 9
                p_new_img.green = (s1.green+s2.green+s3.green+s4.green+s5.green+s6.green+s7.green+s8.green+s9.green)//9
                p_new_img.blue = (s1.blue+s2.blue+s3.blue+s4.blue+s5.blue+s6.blue+s7.blue+s8.blue+s9.blue) // 9
    return new_img


def main():
    """
    Make image become blurred.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
