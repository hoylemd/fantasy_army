from pyglet.window import key
from game.physicalobjects import InertialObject


class Combatant(InertialObject):
    def __init__(self, name="", body_image=None, x=0.0, y=0.0, speed=10,
                 *args, **kwargs):

        super(Combatant, self).__init__(img=body_image, name=name, x=x, y=y,
                                        *args, **kwargs)

        self.speed = speed

        self.center_x = x
        self.center_y = y

        self.key_handler = key.KeyStateHandler()
