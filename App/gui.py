""" Tkinter-based module to create a GUI. """
import tkinter as tk
from tkinter import ttk


class WatermarkApp(tk.Tk):
    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title = "Image Watermark Desktop"
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(True, True)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)


class MainFrame(ttk.Frame):
    """Frame which contains all app widgets."""

    def __init__(self, container):
        super().__init__(container)

        self.img_display = tk.Canvas(
            master=container,
            width=WatermarkApp.WIDTH / 1.5,
            height=WatermarkApp.HEIGHT / 1.5,
        )
        self.img_display.configure(bg="red")  # testing
        self.img_display.grid(row=0, column=2)


# testing
app = WatermarkApp()
MainFrame(app)
app.mainloop()
