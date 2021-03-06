"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
# from evennia import create_script
# from commands.searoom import CoastalCmdSet


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass


class Outside(Room):
    """
    Sea rooms and dry land will inherit from this. Probably where weather
    effects will be defined.

    All Outside rooms have global coordinates and give their position to any
    object they receive.

    Has wind and weather.
    """
    def at_object_receive(self, new_arrival, source_location):
        new_arrival.db.position = self.db.coordinates

    def return_appearance(self, looker):
        """
        This formats a description. It is the hook a 'look' command
        should call.

        Args:
            looker (Object): Object doing the looking.
        """
        if not looker:
            return
        # get and identify all objects
        visible = (con for con in self.contents if con != looker and
                   con.access(looker, "view"))
        exits, users, things = [], [], []
        for con in visible:
            key = con.get_display_name(looker)
            if con.destination:
                exits.append(key)
            elif con.has_player:
                users.append("{c%s{n" % key)
            else:
                things.append(key)
        # get description, build string
        string = "{c%s{n\n" % self.get_display_name(looker)
        desc = self.db.desc
        wind = self.db.wind
        if desc:
            string += "%s" % desc
        if wind:
            string += "The wind is blowing %s knots " % wind[1]
            string += "out of the %s." % wind[0]
        if exits:
            string += "\n{wExits:{n " + ", ".join(exits)
        if users or things:
            string += "\n{wYou see:{n " + ", ".join(users + things)
        return string


class SeaRoom(Outside):
    'Common Parent of master and dynamic sea rooms if needed.'


class DynamicRoom(SeaRoom):
    '''
    Probably all the action should take place here. That is the DSR is the only
    room that players should ever see.  So for instance the command sets should
    apply here etc.
    '''

    '''
    def at_object_leave(self, moved_obj, target_location):
        This function was set up to handle deletion of temporary rooms when no
        longer needed.  not
        print "%s left" % moved_obj
        # if moved_obj was a vessel
        if not moved_obj.is_typeclass("typeclasses.vessel.VesselObject"):
            print "not a vessel though so no worries"
            return

        # then search contents of room for any other vessels
        print "Remaining objects: "
        # print self.contents
        vessel_count = 0
        for floater in self.contents:
            print floater
            if floater.is_typeclass("typeclasses.vessel.VesselObject"):
                vessel_count = vessel_count + 1
        print "vessel count = %s" % vessel_count
        # if any vessels remain, then return
        if vessel_count > 1:
            return
        else:
            # if none, then add the script
            self.scripts.add("typeclasses.scripts.CleanSeaRoom")
    '''
    def at_server_reload(self):
        # this cleans up extra dyanmic rooms if they are not being used.
        if not self.contents:
            print "Cleaning up empty dynamic room"
            self.delete()


# Coastal Rooms
class CoastalRoom(SeaRoom):
    """
    Coastal rooms need to be defined with co-ordinates so that they
    can pass that to vessels that leave them for the sea room giving the
    vessel its starting position at Sea.

    Finally the Sea will need to know where everyroom is so as to deliver
    vessels to the right coastal room as an exit.

    Also I'd like Coastal rooms to have a tag that makes them passable
    by vessels. Default rooms can be presumed to be landrooms and not
    so passable.  Rivers would make an interesting subset of this.
    """
    pass


# Dry land
class DryLandRoom(Outside):
    pass
# Last line
