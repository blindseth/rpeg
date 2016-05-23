from engine.game.move.component import Component

class Repeat(Component):
    """Component that will complete another component x times"""

    def __init__(self, repeat, components):
        """Repeat the given list of components a given number of times.
        repeat -> int
        components -> list Components"""
        self.repeat = repeat
        self.components = components

    def on_cast(self, target, caster, players, monsters):
        msg = ""
        for i in range(self.repeat):
            for component in self.components:
                msg += component.on_cast(
                    target, caster, players, monsters)+'\n'
        return msg