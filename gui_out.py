"""Handle and be the parent of all Output to User."""

import tkinter as tk
from widgets import ScrolledText


class Output(tk.PanedWindow):
    """A user widget used to store output based objects."""

    def __init__(self, w, h, master=None):
        """Create Output object.

        Args:
            w (int): Width
            h (int): Height
            master (tkinter widget, optional): Parent widget. Defaults to None.
        """

        # Construct base
        super().__init__(master, width=w, height=h)
        self.place(bordermode="outside", x=0, y=0)

        self.width = w
        self.height = h

        # Construct the main output
        self.history = ScrolledText(self, self.width, self.height)
        self.history.place(bordermode="outside", x=0, y=0)
