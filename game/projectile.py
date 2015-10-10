from pyglet import clock
from physicalobjects import InertialObject


class Projectile(InertialObject):
    def __init__(self, lifespan=0.5, *args, **kwargs):
        super(Projectile, self).__init__(damaging=True, *args, **kwargs)

        clock.schedule_once(self.die, lifespan)
