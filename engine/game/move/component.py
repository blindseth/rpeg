"""Defines the base class for Component"""

class Component(object):
    """Base Class of All component objects. Describes methods
    that are used in move components"""

    def get_targets(self, selected, caster, players, monsters):
        """Get target returns a list of targets in the form of
        character objects"""
        return []

    def get_miss(self, miss, selected, caster, players, monsters):
        """Returns the miss bound of the move"""
        return miss

    def get_crit(self, crit, selected, caster, players, monsters):
        """Returns the crit bound of the move"""
        return crit

    def on_cast(self, target, caster, players, monsters):
        """Cast of the component move and returns a log
        with a message from that component"""
        return ""

    def valid_targets(self, selected, caster, players, monsters, targets):
        """Returns a if the given targets are valid for the move"""
        return True