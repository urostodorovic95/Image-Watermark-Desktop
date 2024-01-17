""" PIL/PILLOW-based module to deal with image processing. """
from PIL import Image, ImageTk, UnidentifiedImageError


def return_img_from_file(image_path: str) -> Image.Image:
    """Returns a PIL.Image object"""
    try:
        return Image.open(image_path)
    except UnidentifiedImageError:
        return None


def resize_img(original_image: Image.Image, canvas_height: int) -> ImageTk.PhotoImage:
    """Uses original image dimensions and canvas height to return a resized image
    which fits on the canvas."""
    aspect_ratio = original_image.width / original_image.height
    new_width = int(aspect_ratio * canvas_height)
    resized_img = original_image.resize((new_width, canvas_height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_img)


def create_composite(watermark_img_path: str, original_img: Image.Image) -> Image.Image:
    watermark_img = return_img_from_file(watermark_img_path)
    if watermark_img:
        # make watermark the same size as img
        watermark = watermark_img.resize(original_img.size)
        original_img.paste(watermark, (0, 0), watermark)
        return original_img
