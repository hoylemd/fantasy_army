from combatant import Combatant


class Hero(Combatant):
    def __init__(self, *args, **kwargs):
        super(Hero, self).__init__(*args, **kwargs)

        self.heroic = True
