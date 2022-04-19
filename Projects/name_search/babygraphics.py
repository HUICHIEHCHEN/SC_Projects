"""
File: babygraphics.py
Name: Hui-Chieh Chen
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000                             # Width of canvas
CANVAS_HEIGHT = 600                             # Height of canvas
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,    # List of years to be analyzed
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20                          # Distance between line and the edge of canvas
COLORS = ['red', 'purple', 'green', 'blue']     # List of colors used to represent trend lines of different names
TEXT_DX = 2                                     # Distance between line and the left side of text
LINE_WIDTH = 2                                  # Width of a line
MAX_RANK = 1000                                 # The lowest ranking retained in the data for each year


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_distance = (width - GRAPH_MARGIN_SIZE * 2) // len(YEARS)      # The distance of x coordinate between years
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * x_distance
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # Draw bottom horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # Draw vertical lines representing the years at equal intervals
    for i in range(len(YEARS)):
        l_x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(l_x, 0, l_x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(l_x + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    y_distance = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK     # The distance of y coordinate between each rank
    for idx, target in enumerate(lookup_names):        # idx refers to the index of the target
        data_x = []        # Save x coordinate of each data
        data_y = []        # Save y coordinate of each data
        color = COLORS[idx % len(COLORS)]
        for i in range(len(YEARS)):
            data_x.append(get_x_coordinate(CANVAS_WIDTH, i))
            if str(YEARS[i]) in name_data[target]:        # Data of the target is available for the given year
                rank = name_data[target][str(YEARS[i])]
                data_y.append(GRAPH_MARGIN_SIZE + int(rank) * y_distance)
                canvas.create_text(data_x[i] + TEXT_DX, data_y[i], text=target+' '+rank, anchor=tkinter.SW, fill=color)
            else:
                data_y.append(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                canvas.create_text(data_x[i] + TEXT_DX, data_y[i], text=target+' '+'*', anchor=tkinter.SW, fill=color)
            if i > 0:        # Connect the latest data point with previous one to create line
                canvas.create_line(data_x[i-1], data_y[i-1], data_x[i], data_y[i], width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
