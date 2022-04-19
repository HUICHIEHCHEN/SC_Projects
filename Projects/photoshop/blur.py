"""
File: blur.py
Name: Hui-Chieh Chen
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    Create a blurred image by changing each pixel's RGB value to the average
    RGB values of that pixel and its nearest neighbors
    ---------------------------------------------------
    :param img: SimpleImage, the original image
    :return: SimpleImage, blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = new_img.get_pixel(x, y)
            # Total values of R,G,B
            total_r = 0
            total_g = 0
            total_b = 0
            neighbor = 0   # Number of neighbors
            for move_x in range(-1, 2):   # For x-1, x, x+1
                for move_y in range(-1, 2):   # For y-1, y, y+1
                    # Get x, y coordinates of neighboring pixels
                    neighbor_x = move_x + x
                    neighbor_y = move_y + y
                    if 0 <= neighbor_x < img.width and 0 <= neighbor_y < img.height:
                        total_r += img.get_pixel(neighbor_x, neighbor_y).red
                        total_g += img.get_pixel(neighbor_x, neighbor_y).green
                        total_b += img.get_pixel(neighbor_x, neighbor_y).blue
                        neighbor += 1
            pixel.red = total_r / neighbor
            pixel.green = total_g / neighbor
            pixel.blue = total_b / neighbor
    return new_img


def main():
    """
    This function shows the original image first, then its blurred image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
