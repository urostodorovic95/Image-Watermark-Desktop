""" Tkinter-based module to create a GUI. """
import tkinter as tk
from tkinter import ttk, filedialog
import img_processing


class WatermarkApp(tk.Tk):
    """Main window config."""

    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("Image Watermark Desktop")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)


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
        self.img_display.configure(bg="grey")
        self.no_img_msg = self.img_display.create_text(
            250,
            200,
            text="No image loaded. Load an image and a preview will be shown here.",
        )
        self.img_display.grid(row=2, column=2)

        # load button
        self.load_button = ttk.Button(
            master=container, text="2. Load Image", command=self.load_image_from_file
        )
        self.load_button.grid(row=1, column=2, sticky="N")

        # watermark image
        self.watermark_path = None
        self.watermark_img_button = ttk.Button(
            master=container, text="1. Load Watermark", command=self.load_watermark_path
        )
        self.watermark_img_button.grid(row=0, column=2, sticky="S")

    def load_image_from_file(self):
        selected_img_path = filedialog.askopenfilename(
            title="Select an image", filetypes=[("All files", "*")]
        )
        pillow_img = img_processing.return_img_from_file(selected_img_path)
        if pillow_img:
            tk_img = img_processing.resize_img(
                pillow_img, self.img_display.winfo_height()
            )
            # update the canvas with image
            self.img_display.create_image(
                self.img_display.winfo_width() / 2,
                self.img_display.winfo_height() / 2,
                image=tk_img,
            )
            self.img_display.img = tk_img  # needed to bypass garbage collector
            # remove canvas bg by setting a default color; remove text
            self.img_display.config(bg=f"{tk.Canvas()['background']}")
            self.img_display.itemconfig(self.no_img_msg, text="")

    def load_watermark_path(self):
        watermark_path = filedialog.askopenfilename(
            title="Select watermark", filetypes=[("All files", "*")]
        )
        self.watermark_img_button.config(text=f"...{watermark_path[-15:]}✅")


# testing
app = WatermarkApp()
MainFrame(app)
app.mainloop()
