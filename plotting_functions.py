# this file contains functions to plot data

from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def simple_plot(root):
    px = 1/plt.rcParams['figure.dpi']
    print(px, plt.rcParams['figure.dpi'])
    fig = plt.Figure(figsize=(root.graphic_frame_width*px, root.graphic_frame_height*px), dpi=130)
    print(px, plt.rcParams['figure.dpi'])
    a = fig.add_subplot(111)
    a.scatter(root.motion_data['x'], root.motion_data['y'], color='blue')
    a.invert_yaxis()

    a.set_title("2D plot", fontsize=16)
    a.set_ylabel("Y", fontsize=14)
    a.set_xlabel("X", fontsize=14)
    #a.set_position([0, 0, 1, 1])

    canvas = FigureCanvasTkAgg(fig, master=root.left_frame)
    canvas.get_tk_widget().grid(column=0, row=0)
    root.left_frame.grid_rowconfigure(0, weight=2, uniform=1)
    root.left_frame.grid_propagate(False)
    canvas.draw()
    return canvas


