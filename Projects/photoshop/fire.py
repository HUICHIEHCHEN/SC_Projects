"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image
    :return: SimpleImage, the updated image with specific areas highlighted and the rest in grayscale
    """
    highlight_img = SimpleImage(filename)
    for pixel in highlight_img:
        avg = (pixel.red+pixel.green+pixel.blue)/3
        if pixel.red > avg * HURDLE_FACTOR:  # Highlight pixels that are recognized as fire
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:  # Grayscale
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return highlight_img


def main():
    """
    This file first shows the original image, followed by its grayscale
    image, where the highlighted pixels are the ones identified as fire
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
