"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    Create a new image that shrinks the width and height of the
    original image by half
    ---------------------------------------------------
    :param filename: str, the filepath of the original image
    :return img: SimpleImage, the image that after shrinking the original image
    """
    img = SimpleImage(filename)
    shrink_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(shrink_img.width):
        for y in range(shrink_img.height):
            img_p = img.get_pixel(x*2, y*2)
            #  Place the pixels where both x and y are even numbers on the new canvas
            sr_p = shrink_img.get_pixel(x, y)
            sr_p.red = img_p.red
            sr_p.green = img_p.green
            sr_p.blue = img_p.blue
    return shrink_img


def main():
    """
    This file shows the original image first, then a scaled-down version
    of the original image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
