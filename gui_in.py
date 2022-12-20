"""Handle, or at lease be the parent of, all input related stuff."""

import tkinter as tk
from typewriter import write
from widgets import EntryButton


class Input(tk.PanedWindow):
    """A user widget used to store input based objects."""

    def __init__(self, w, h, master=None):
        """Construct Input object.

        Args:
            w (int): Width
            h (int): Height
            master (tkinter widget, optional): Parent widget. Defaults to None.
        """

        # Construct base
        super().__init__(master, bg="white", borderwidth=3)
        self.place(
            bordermode="outside",
            anchor="sw",
            width=w,
            height=h,
            x=0,
            rely=1,
        )

        self.width = w
        self.height = h
