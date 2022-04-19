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
    :param filename: str, the file path of the original image
    :return: SimpleImage, a vertical mirror image of the original image
    """
    img = SimpleImage(filename)
    r_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)  # Original pixel
            r_p1 = r_img.get_pixel(x, y)  # Top of the blank canvas
            r_p2 = r_img.get_pixel(x, r_img.height-1-y)  # Bottom of the blank canvas
            r_p1.red = img_p.red
            r_p1.green = img_p.green
            r_p1.blue = img_p.blue
            r_p2.red = img_p.red
            r_p2.green = img_p.green
            r_p2.blue = img_p.blue
    return r_img


def main():
    """
    This file contains one image processing algorithm that produce
    a mirrored version of the original image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
