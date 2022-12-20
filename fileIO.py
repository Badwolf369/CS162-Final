"""Deal with all needed file I/O"""


def get_msgs():
    """Get the saved messages from the file.

    Returns:
        str: Messages in file
    """

    with open("paper.txt", "r") as f:
        return f.read()


def add_msg(msg):
    """Add MSG to the file as a new message.

    Args:
        msg (str): Message to add to file
    """

    with open("paper.txt", "a") as f:
        f.write(f" - {msg}\n")
