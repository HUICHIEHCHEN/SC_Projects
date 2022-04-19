"""
File: draw_line.py
Name: Hui-Chieh Chen
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of circle
SIZE = 10

window = GWindow()

# Records the number of clicks
count = 1

# Records the x, y coordinates of circle
# old_x = 0
# old_y = 0
circle = GOval(SIZE * 2, SIZE * 2)


def main():
    onmouseclicked(connect)
    circle.color = 'black'
    circle.filled = False


def connect(mouse):
    global count   # old_x, old_y
    if count % 2 != 0:  # The number of clicks is odd
        # circle = GOval(SIZE*2, SIZE*2)
        # circle.color = 'black'
        # circle.filled = False
        window.add(circle, x=mouse.x-SIZE, y=mouse.y-SIZE)
        # Record x, y coordinates of the center of circle
        old_x = circle.x + SIZE
        old_y = circle.y + SIZE
    else:  # The number of clicks is even
        # circle = window.get_object_at(old_x, old_y)
        line = GLine(circle.x+SIZE, circle.y+SIZE, mouse.x, mouse.y)
        window.remove(circle)
        window.add(line)
    count += 1


if __name__ == "__main__":
    main()
