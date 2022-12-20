"""A library containing all my costom widgets."""

import tkinter as tk


class DoubleButton(tk.PanedWindow):
    """Like a tkinter Button but it's 2 buttons in one."""

    def __init__(self, master, w, h, msgs, cmds):
        """Create a DoubleButton widget.

        Args:
            master (tkinter widget): Parent widget
            w (int): Width
            h (int): Height
            msgs (list): Text for each button; len() must be 2
            cmds (list): Commands for each button; len() must be 2
        """
        #
        # Construct base
        super().__init__(master, width=w, height=h)
        # Construct first button
        self.b0 = tk.Button(self, text=msgs[0], command=cmds[0])
        self.b0.place(
            bordermode="outside",
            anchor="center",
            width=int(w / 2),
            height=h,
            relx=0.25,
            rely=0.5,
        )
        # Construct second button
        self.b1 = tk.Button(self, text=msgs[1], command=cmds[1])
        self.b1.place(
            bordermode="outside",
            anchor="center",
            width=int(w / 2),
            height=h,
            relx=0.75,
            rely=0.5,
        )


class TripleButton(tk.PanedWindow):
    """Like a tkinter button but it's 3 buttons in one."""

    def __init__(self, master, w, h, msgs, cmds):
        """Create a TripleButton widget.

        Args:
            master (tkinter widget): Parent widget
            w (int): Width
            h (int): Height
            msgs (list): Text for each button; len() must be 3
            cmds (list): Commands for each button; len() must be 3
        """

        # Construct base
        super().__init__(master, width=w, height=h, bg="black")
        # Construct first button
        self.b0 = tk.Button(self, text=msgs[0], command=cmds[0])
        self.b0.place(
            bordermode="outside",
            anchor="center",
            width=w // 3,
            height=h,
            relx=0.5 - (1 / 3),
            rely=0.5,
        )
        # Construct second button
        self.b1 = tk.Button(self, text=msgs[1], command=cmds[1])
        self.b1.place(
            bordermode="outside",
            anchor="center",
            width=w // 3,
            height=h,
            relx=0.5,
            rely=0.5,
        )
        # Construct third button
        self.b2 = tk.Button(self, text=msgs[2], command=cmds[2])
        self.b2.place(
            bordermode="outside",
            anchor="center",
            width=w // 3,
            height=h,
            relx=0.5 + (1 / 3),
            rely=0.5,
        )


class ScrolledText(tk.PanedWindow):
    """Basic text widget with a Scrollbar on the right side."""

    def __init__(self, master, w, h):
        """Create a ScrolledText widget.

        Args:
            master (tkinter widget): Parent widget
            w (int): Width
            h (int): Height
        """

        # Had to get creative here because the text and the scroll bar
        # both reference each other.
        super().__init__(master, width=w, height=h)
        self.text = tk.Text(self)
        self.scroll = tk.Scrollbar(self)

        self.text.config(
            state="disabled", yscrollcommand=self.scroll.set
        )
        self.text.place(
            bordermode="outside", x=0, y=0, width=w - 20, height=h
        )

        self.scroll.config(
            orient="vertical", command=self.text.yview
        )
        self.scroll.place(
            bordermode="outside",
            anchor="e",
            x=w,
            rely=0.5,
            width=20,
            height=h,
        )

    def addText(self, text):
        """Add text to the widget.

        Args:
            text (str): Text to add into the widget
        """

        # Have to change these states so User cant type in the text widget,
        # but also so I can insert text.
        self.text.config(state="normal")
        self.text.insert(tk.END, text)
        self.text.config(state="disabled")


class EntryButton(tk.PanedWindow):
    """Entry with an attached button."""

    def __init__(self, master, w, h, text, cmd):
        """Create EntryButton widget.

        Args:
            master (tkinter widget): Parent widget
            w (int): Width
            h (int): Height
            text (str): Text for button
            cmd (function): Command for button
        """
        # Construct base
        super().__init__(master, width=w, height=h)

        # Construct button
        self.button = tk.Button(self, text=text, command=cmd,)
        self.button.place(
            bordermode="outside",
            anchor="center",
            relx=0.5,
            rely=0.75,
        )

        # Construct entry
        self.entryVal = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entryVal)
        self.entry.place(
            bordermode="outside",
            anchor="center",
            relx=0.5,
            rely=0.25,
        )
