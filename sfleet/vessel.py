from game.physicalobjects import InertialObject
from game.scalar import Scalar


class Vessel(InertialObject):
    def __init__(self, name="", hull_image=None, spec=None,
                 *args, **kwargs):

        super(Vessel, self).__init__(img=hull_image, name=name,
                                     *args, **kwargs)

        self.speed = spec['speed']
        self.hull = Scalar(spec['hull'])
        self.armour = Scalar(spec['armour'])
        self.armour_threshold = spec['armour_threshold']
        self.shield = Scalar(spec['shield'])
        self.shield_recharge = spec['shield_recharge']

        self.weapon_range = spec['weapon_range']
        self.weapon_damage = spec['weapon_damage']
