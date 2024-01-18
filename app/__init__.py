""" Initalize the app. """
from . import gui


def watermark_app():
    """Create the app."""
    app = gui.WatermarkApp()
    gui.MainFrame(app)
    app.mainloop()
