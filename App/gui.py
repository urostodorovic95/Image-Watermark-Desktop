""" Tkinter-based module to create a GUI. """
import tkinter as tk
from tkinter import ttk


class WatermarkApp(tk.Tk):
    """Main window config."""

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

    CANVAS_SIZE_RATIO = 1.5

    def __init__(self, container):
        super().__init__(container)

        # canvas to display the user image
        self.img_display = tk.Canvas(
            master=container,
            width=WatermarkApp.WIDTH / self.CANVAS_SIZE_RATIO,
            height=WatermarkApp.HEIGHT / self.CANVAS_SIZE_RATIO,
        )
        self.img_display.configure(bg="red")  # testing
        self.img_display.grid(row=2, column=2)

        # load button
        self.load_button = ttk.Button(
            master=container, text="Load image", command=self.load_image_from_file
        )
        self.load_button.grid(row=0, column=2)

    def load_image_from_file(self):
        pass


# testing
app = WatermarkApp()
MainFrame(app)
app.mainloop()
