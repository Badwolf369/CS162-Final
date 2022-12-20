"""The entire base story that drives the game.

Its all dumped in here so that I dont have to clutter
the other modules with the story.

This story is based off the first program I ever wrote titled Adventure.py
You're welcome to look at it, it should be in the root.
I wrote it when I was like 10 so its quite bad.
(It doesnt work so dont try to play it. It was written in python 2 I think.
Though it doesnt work in that either.)
"""

from fibonacci import fibonacci
from fileIO import get_msgs


class Story:
    """Collection of all the story elements."""

    def __init__(self):
        """Make all the story variables available."""

        # Clipping line used to keep the text wrapping from cutting words.
        # --------------------------------------------------#

        # bad decision
        self.death = (
            "YOU HAVE DIED.\n" + "Restart the game to continue..."
        )

        # start
        self.msg_0 = (
            "Welcome!\n"
            + "This is a story about, erm, well I don't know.\n"
            + "But you're him.\n"
            + "You're walking down a path in the jungle.\n"
            + "You come to a fork.\n"
            + "Do you want to go left, straight, or right?\n"
            + "(Probably dont go straight)\n"
        )

        # left
        self.msg_00 = (
            "You turn left and continue along the path.\n"
            + "You hear a rustling behing you.\n"
            + "You start walking a bit faster.\n"
            + "Suddenly, a man jumps out of the bushes in front\n"
            + "of you.\n"
            + "The man has strange tatoos and paint all over his\n"
            + "body.\n"
            + "He also carries a spear arnamented with colorful\n"
            + "ribbons.\n"
            + "Do you run, try to talk to him, or try to fight\n"
            + "him?\n"
        )

        # run
        self.msg_000 = (
            "You turn back and run the other way.\n"
            + "You hear him yell something behind you.\n"
            + "Suddenly, a dozen other similar men jump out of\n"
            + "the bushes, surrounding you.\n"
            + "They are head hunters.\n"
            + "They take you back to their camp, where your head\n"
            + "will likely be removed.\n"
            + self.death
        )

        # talk
        self.msg_001 = (
            "You begin trying to talk to him.\n"
            + "He says something and 3 similar men jump out of\n"
            + "the bushes and grab you.\n"
            + "They are head hunters.\n"
            + "They take you back to their camp, where your head\n"
            + "will likely be removed.\n"
            + self.death
        )

        # fight
        self.msg_002 = (
            "You run at him to shove him over.\n"
            + "A dozen similar men jump out of the bushes around\n"
            + "you, surrounding you.\n"
            + "They are head hunters.\n"
            + "They take you back to their camp, where your head\n"
            + "will likely be removed.\n"
            + self.death
        )

        # straight
        self.msg_01 = (
            "You go straight.\n"
            + "Stuff starts looking wierd and warpy around you.\n"
            + "Suddenly everything goes black.\n"
            + "You wake up in a strange white room.\n"
            + "In front of you are two objects.\n"
            + "The first is a strange spiral looking object with\n"
            + "numbers inscribed on it.\n"
            + "The second is an extremely old looking paper with\n"
            + "a pen and ink pot next to it.\n"
            + "Which would you like to examine closer?\n"
        )

        # Spiral
        nums = fibonacci(100)
        fibo = ""
        for i in nums:
            fibo += f"-{str(i)} \n"
        self.msg_010 = (
            "You examine the strange spiraling object.\n"
            + "The strange numbers begin to glow then suddenly stop.\n"
            + "Then suddenly the...wait what?...The narrator\n"
            + "cuts out? Why??\n"
            + "Wait who are you? What are you doing??\n"
            + "NO THATS MI-\n"
            + "...\n"
            + "...\n"
            + "...\n"
            + fibo
        )

        # Paper
        self.msg_011 = (
            "You go and examine the paper.\n"
            + "Written on the paper is the following:\n"
            + get_msgs()
            + "Would you like to leave a message?\n"
        )

        # Yes, after message has been entered
        self.msg_0110 = (
            "You write the message onto the paper.\n"
            + "As soon as you are finished, you drop down onto\n"
            + "the ground, completely unable to move your arms\n"
            + "or legs as your view fades to black.\n"
            + self.death
        )

        # No
        self.msg_0111 = (
            "You try to look away from the paper,\n"
            + "but as you do so, your entire body becomes limp.\n"
            + "You lay there struggling to move as your view\n"
            + "slowly fades to black.\n"
            + self.death
        )

        # right
        self.msg_02 = (
            "You turn right and continue along the path.\n"
            + "You see something sparkle in the path at your\n"
            + "feet.\n"
            + "Do you ignore it and move on or look closer?\n"
        )

        # ignore both times
        self.msg_020 = (
            "You ignore it and move on.\n"
            + "You see a rainbow off in the distance.\n"
            + "You remember those old fairy tales about the pot\n"
            + "of gold at the end of the rainbow.\n"
            + "Go to the rainbow to get the gold?"
        )

        # look closer
        self.msg_021 = (
            "You examine the shiny thing closer.\n"
            + "It is a perfect ruby embedded in the trail!\n"
            + "Do you ignore it or try to pick it up?\n"
        )

        # pick it up; ignoring skips back to 020
        self.msg_0211 = (
            "You attempt to pick it up.\n"
            + "It seems to be stuck.\n"
            + "You pry harder.\n"
            + "You feel a rumbling beneath you.\n"
            + "Suddenly, out of the ground bursts an enourmous\n"
            + "bronze Serpent, with ruby eyes.\n"
            + "It opens its mouth and strikes, gobbling you up\n"
            + "in one bite.\n"
            + self.death
        )
