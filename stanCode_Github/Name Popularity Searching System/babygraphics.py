"""
File: babygraphics.py
Name: 
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
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


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
    x_coordinate = GRAPH_MARGIN_SIZE + (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


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
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_flag = 0
    for name in lookup_names:
        color_flag += 1
        for i in range(len(YEARS) - 1):
            """
            get the rank for a name in a specified year
            and handle the case when a name is not in the rank list of a specified year
            """
            if str(YEARS[i]) not in name_data[name]:
                rank_y0 = '*'
            else:
                rank_y0 = int(name_data[name][str(YEARS[i])])
            if str(YEARS[i+1]) not in name_data[name]:
                rank_y1 = '*'
            else:
                rank_y1 = int(name_data[name][str(YEARS[i+1])])
            # ---------------------------
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                               get_y_coordinate(CANVAS_HEIGHT, rank_y0),
                               get_x_coordinate(CANVAS_WIDTH, i+1),
                               get_y_coordinate(CANVAS_HEIGHT, rank_y1),
                               fill=COLORS[(color_flag-1)%len(COLORS)],
                               width=LINE_WIDTH)
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
                               get_y_coordinate(CANVAS_HEIGHT, rank_y0),
                               text=name + " " + str(rank_y0),
                               anchor=tkinter.SW)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i+1) + TEXT_DX,
                           get_y_coordinate(CANVAS_HEIGHT, rank_y1),
                           text=name + " " + str(rank_y1),
                           anchor=tkinter.SW)


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of a name,
    returns the y coordinate of the rank on the canvas.

    Input:
        height (int): The height of the canvas
        rank (int/str): The rank of a specified name. It would be '*'(str) if the name is not in the rank list.
    Returns:
        y_coordinate (int): The y coordinate of the rank on the canvas.
    """
    if rank == '*':
        rank = 1000
    y_coordinate = int(GRAPH_MARGIN_SIZE + (height - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * (rank - 1))
    return y_coordinate


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
