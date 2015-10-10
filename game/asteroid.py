from random import randint, uniform
from physicalobjects import InertialObject


class Asteroid(InertialObject):
    def __init__(self, explosive_force=70.0, *args, **kwargs):
        super(Asteroid, self).__init__(vulnerable=True, damaging=True,
                                       *args, **kwargs)
        self.explosive_force = explosive_force

    def handle_collision(self, other):
        super(Asteroid, self).handle_collision(other)

        if self.dead and self.scale > 0.25:
            num_fragments = randint(2, 3)

            for i in xrange(num_fragments):
                new_asteroid = Asteroid(img=self.image,
                                        explosive_force=self.explosive_force,
                                        x=self.x, y=self.y, batch=self.batch)

                new_asteroid.rotation = randint(0, 360)
                explosion_rotation = uniform(-1.0, 1.0) * self.explosive_force
                new_asteroid.rotation_speed = (
                    self.rotation_speed + explosion_rotation)

                explosion_vx = uniform(-1.0, 1.0) * self.explosive_force
                new_asteroid.velocity_x = self.velocity_x + explosion_vx

                explosion_vy = uniform(-1.0, 1.0) * self.explosive_force
                new_asteroid.velocity_y = self.velocity_y + explosion_vy

                new_asteroid.scale = self.scale / 2.0

                self.new_objects.append(new_asteroid)

    def update(self, dt):
        super(Asteroid, self).update(dt)
