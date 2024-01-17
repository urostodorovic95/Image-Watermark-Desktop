""" Tkinter-based module to create a GUI. """
import tkinter as tk
from tkinter import ttk


class WatermarkApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title = "Image Watermark Desktop"
        self.geometry("800x600")
        self.resizable(True, True)


# testing
app = WatermarkApp()
app.mainloop()
