"""Pretty much run the entire game."""

import tkinter as tk

from gui_out import Output
from gui_in import Input
from story import Story
from typewriter import write
from widgets import DoubleButton, TripleButton, EntryButton
from fileIO import add_msg


class Choice(tk.PanedWindow):
    """A way to view and manage each choice as an object."""

    def __init__(
        self, master, w, h, oup, inp, message, choices, results
    ):
        """Construct the Choice widget with parent MASTER.

        Args:
            master (tkinter widget): widget's master
            w (int): width of widget
            h (int): height of widget
            oup (tk.PanedWindow): Output pane
            inp (tk.PanedWindow): Input pane
            message (str): Message preceding craetion of buttons
            choices (list): Text for buttons; len() of 2 or 3
            results (list): Commands for buttons; len() of 2 or 3
        """

        # Build base
        super().__init__(master, width=w, height=h)
        self.place(bordermode="outside", x=0, y=0)

        # make sure RESULTS and CHOICES work together
        if len(choices) != len(results):
            raise Exception(
                "len() of RESULTS and CHOICES not the same."
            )

        self.choices = choices
        self.results = results
        self.output = oup
        self.input = inp
        self.width = w
        self.height = h

        write(message, oup, self.create_buttons)

    def create_buttons(self):
        """Create the buttons after MESSAGE has been written."""

        if len(self.choices) == 2:
            self.button = DoubleButton(
                self,
                self.width,
                self.height,
                self.choices,
                self.results,
            )
        elif len(self.choices) == 3:
            self.button = TripleButton(
                self,
                self.width,
                self.height,
                self.choices,
                self.results,
            )
        else:
            raise Exception("2 or 3 choices only.")
        self.button.place(bordermode="outside", x=0, y=0)


class Game:
    """Container for all of the game logic."""

    def __init__(self, w, h, root):
        """Create container for all of the game logic and start game.

        Args:
            w (int): Width
            h (int): Height
            root (tkinter widget): parent widget
        """

        self.output = Output(w, h - 100, root)
        self.input = Input(w, 100, root)
        self.story = Story()
        self.width = w
        self.height = h

        self.choice0()

    # Start
    def choice0(self):
        """Create the first choice."""

        self.curChoice = Choice(
            self.input,
            self.width,
            100,
            self.output,
            self.input,
            self.story.msg_0,
            ["Left", "Straight", "Right"],
            [self.choice00, self.choice01, self.choice02],
        )

    # Left
    def choice00(self):
        """Create Level 2 choice."""

        self.curChoice.destroy()
        self.curChoice = Choice(
            self.input,
            self.width,
            100,
            self.output,
            self.input,
            self.story.msg_00,
            ["Run", "Talk", "Fight"],
            [self.death000, self.death001, self.death002],
        )

    # Run
    def death000(self):
        """Show death message."""

        self.curChoice.destroy()
        write(self.story.msg_000, self.output)

    # Talk
    def death001(self):
        """Show death message."""

        self.curChoice.destroy()
        write(self.story.msg_001, self.output)

    # Fight
    def death002(self):
        """Show death message."""

        self.curChoice.destroy()
        write(self.story.msg_002, self.output)

    # Straight
    def choice01(self):
        """Create level 2 choice."""

        self.curChoice.destroy()
        self.curChoice = Choice(
            self.input,
            self.width,
            100,
            self.output,
            self.input,
            self.story.msg_01,
            ["Spiral", "Paper"],
            [self.death010, self.choice011],
        )

    # Spiral
    def death010(self):
        """Show fibonacci sequence."""

        self.curChoice.destroy()
        write(self.story.msg_010, self.output)

    # Paper
    def choice011(self):
        """Create level 3 choice."""

        self.curChoice.destroy()
        self.curChoice = Choice(
            self.input,
            self.width,
            100,
            self.output,
            self.input,
            self.story.msg_011,
            ["Yes", "No"],
            [self.choice0110, self.death0111],
        )

    # Yes
    def choice0110(self):
        """Create the entry to grab the mesage."""

        self.curChoice.destroy()
        self.curChoice = EntryButton(
            self.input, self.width, 100, "Done", self.death0110
        )
        self.curChoice.place(bordermode="outside", x=0, y=0)

    # Done
    def death0110(self):
        """Print the reasult of choice0110."""

        add_msg(self.curChoice.entryVal.get())
        self.curChoice.destroy()
        write(self.story.msg_0110, self.output)

    # No
    def death0111(self):
        """Create a level 4 choice."""

        self.curChoice.destroy()
        write(self.story.msg_0111, self.output)

    # Right
    def choice02(self):
        """Create level 2 choice."""

        self.curChoice.destroy()
        self.curChoice = Choice(
            self.input,
            self.width,
            100,
            self.output,
            self.input,
            self.story.msg_02,
            ["Ignore", "Look closer"],
            [self.choice020, self.choice021],
        )

    # Ignore
    def choice020(self):
        """Create level 3 choice."""

        self.curChoice.destroy()
        write(self.story.msg_020, self.output)

    # Look Closer
    def choice021(self):
        """Craete level 3 choice."""

        self.curChoice.destroy()
        self.curChoice = Choice(
            self.input,
            self.width,
            100,
            self.output,
            self.input,
            self.story.msg_021,
            ["Ignore", "Pick up"],
            [self.choice020, self.death0211],
        )

    # Pick Up
    def death0211(self):
        """Show death message."""

        self.curChoice.destroy()
        write(self.story.msg_0211, self.output)
