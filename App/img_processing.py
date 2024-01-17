""" PIL/PILLOW-based module to deal with image processing. """
from PIL import Image, ImageTk


def return_img_from_file(image_path):
    return ImageTk.PhotoImage(Image.open(image_path))
