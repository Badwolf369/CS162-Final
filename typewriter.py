"""Quick helper program that will create a typing effect."""

from random import randint as rand


def write(msg, output=None, cmd=None):
    """Create a typing effect in OUTPUT then run CMD.

    Args:
        msg (str): Text to type.
        output (tk.PanedWindow, optional): Output to type to. Defaults to None.
        cmd (function, optional): Run after done typing. Defaults to None.
    """

    # This code block is slightly bizzare so I need to explain.
    # This essentially stops the typing effect if a new one is started.
    # To do this I nee dthe value retuned by widget.after()
    # which here is stc (Stop Typing Code).
    # However the first time the program runs, this doesnt exist,
    # hence the try/except.
    # To make things simpler, the check 'if stc is None' creates the
    # same error as if the code did not exist.

    try:
        if output.stc is None:
            raise AttributeError()
        output.after_cancel(output.stc)
        output.history.addText("\n")
    except AttributeError:
        pass

    # formats the string
    msg = str(msg)
    msgs = msg.splitlines()

    def iter_lines(lns, ln=0):
        """Seudo-recursively iterate over all the lns using .after().

        Args:
            lns (list): List of lines
            ln (int, optional): Index of the current line. Defaults to 0.
        """

        def iter_chars(lns, chars, c=0):
            """Seudo-recursively iterate over chars .after()

            Args:
                lns (list): List of lines
                chars (str): Current line or characters
                c (int, optional): Index of current char. Defaults to 0.
            """

            try:
                # Write char and S-recurse to the next char
                output.history.addText(chars[c])
                output.stc = output.after(
                    rand(10, 50), iter_chars, lns, chars, c + 1
                )

            # Stop S-recursing if you walk off the end of the list
            except IndexError:
                # Move on to next line
                output.history.addText("\n")
                output.stc = output.after(
                    500, iter_lines, lns, ln + 1
                )
                return

        try:
            # Begin S-recuring over current line
            iter_chars(lns, lns[ln])

        # Stop S-Recursing if you walk off the end of the list
        except IndexError:
            # End the function and run the given command
            output.stc = None
            if cmd is not None:
                cmd()
            return

    # Begin S-Recursing over the lines.
    iter_lines(msgs)
