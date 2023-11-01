# this is test of tkinter
import os
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import loading_and_saving_functions as lsf
import processing_functions as pf

from plotting_functions import simple_plot

class WindowDesign:

    @classmethod
    def get_dir_path(self, root):
        root.path = tk.filedialog.askdirectory()
        os.chdir(root.path)


    @classmethod
    def get_file_name(self, root):

        if not hasattr(root, 'path'):
            self.get_dir_path(root)

        root.filename = filedialog.askopenfilename(initialdir=root.path, title="Select file",
                                                   filetypes=(("JSON", "*.json"), ("all files", "*.*")))

        root.motion_data = lsf.data_reader(root.filename)
        root.motion_data = pf.get_dataframe(root.motion_data)

        canvas = simple_plot(root)



        print('completed ', root.filename)

    def __init__(self):
        root = tk.Tk()
        root.minsize(1600, 800)
        root.title("DraWrite Explorer")
        root.wm_iconbitmap("icon_name.ico")

        menubar = tk.Menu(root)

        root.config(menu=menubar)

        file_menu = tk.Menu(menubar)

        file_menu.add_command(label='Open', command=lambda: self.get_file_name(root))
        file_menu.add_command(label='Browse', command=lambda: self.get_dir_path(root))

        menubar.add_cascade(
             label="File",
             menu=file_menu,
         )

        file_menu.add_command(
             label='Exit',
             command=root.destroy,
         )

        root.graphic_frame_width = 700
        root.graphic_frame_height = 700
        root.left_frame = tk.Frame(root, width=700, height=700, bg='grey')
        root.left_frame.grid(row=0, column=0, padx=1, pady=5)

        root.right_frame = tk.Frame(root, width=700, height=700, bg='grey')
        root.right_frame.grid(row=0, column=1, padx=1, pady=5)


        root.mainloop()

WindowDesign()

