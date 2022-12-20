"""Run to start the program."""

import tkinter as tk
from manager import Game


def main():
    """Start the program."""
    width = 420
    height = 750
    root = tk.Tk()
    main_pane = tk.PanedWindow(root, width=width, height=height)
    main_pane.pack()
    Game(width, height, main_pane)
    root.mainloop()


if __name__ == "__main__":
    main()
