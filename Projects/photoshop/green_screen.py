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
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, the figure image with green screen
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            fg_p = figure_img.get_pixel(x, y)
            bigger = max(fg_p.red, fg_p.blue)  # Find the bigger value in fg_p.red and fg_p.blue
            if fg_p.green > bigger * 2:
                bg_p = background_img.get_pixel(x, y)
                fg_p.red = bg_p.red
                fg_p.green = bg_p.green
                fg_p.blue = bg_p.blue
    return figure_img


def main():
    """
    This function conducts green screen replacement and
    photoshop a person onto background image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
