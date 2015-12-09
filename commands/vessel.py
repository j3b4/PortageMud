# Commands for Ships and Boats etc.

from evennia import Command, CmdSet
# from evennia import default_cmds

"""
TODO: Commands for navigation.  Set Course. 

"""

class CmdBoard(Command):
    """
    boarding a vessel

    Usage:
        board <vessel>

    This command is available to players in the same location
    as the vessel and allows them to embark.
    """

    key = "board"
    aliases = ["embark", "board ship", "come aboard", ]
    help_category = "Mutinous Commands"
    locks = "cmd:not cmdinside()"

    # adding a parser? or something to allow multiple vessels in one room.

    def func(self):
        vessel = self.obj
        self.caller.msg("You board the vessel")
        self.caller.move_to(vessel)


class CmdDebark(Command):
    """
    disembark or deboard from a vessel. Come ashore.

    Usage:
        debark

    This command is available when you are on a vessel. It will move you to the
    room presently containing the vessel.

    TODO:  debark from one ship to another or create a "transfer" command.
    """

    key = "debark"
    aliases = ["disembark", "deboard", "land", "come ashore", ]
    help_category = "Mutinous Commands"
    locks = "cmd:cmdinside()"

    def func(self):
        vessel = self.obj
        parent = vessel.location
        self.caller.move_to(parent)


class CmdLookout(Command):
    # Trying to overload the look command so that it behaves
    # differently when called by a character on a vessel.
    """
    Look around yourself while on board a vessel.

    Usage: look

    This command is available when you are on a vessel. It will
    describe the boat or boat-section you are in as well as the area
    the boat is presently passing through.
    """
    key = "lookout"
    aliases = ["lo","ken","conn", ]

    def func(self):
        # if the looker is not in the boat then return a default look
        # if the looker is inside the boat then add value and return
        vessel = self.obj
        outside = vessel.location
        if self.caller.location == vessel:
            self.msg("You are on a %s.\nOutside you see:\n" % vessel.key)
            self.msg(vessel.at_look(vessel.location))
        elif self.caller.location == outside:
            self.msg("You are not on board trying to lookout")
        else:
            self.msg("Something went wrong with the Lookout Command!")




class CmdSetVessel(CmdSet):
    "Add these commands to the vessel when it is created."

    def at_cmdset_creation(self):
        self.add(CmdBoard())
        self.add(CmdDebark())
        self.add(CmdLookout())

# last line
