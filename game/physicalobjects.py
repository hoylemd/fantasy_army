import pyglet
import game.utils as utils


class InertialObject(pyglet.sprite.Sprite):

    def __init__(self, name="", vulnerable=False, damaging=False,
                 *args, **kwargs):
        super(InertialObject, self).__init__(*args, **kwargs)

        self.name = name
        self.dead = False
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.rotation_speed = 0.0

        self.new_objects = []

    def die(self, dt=0.0):
        self.dead = True

    def collides_with(self, other):
        collision_distance = (self.width / 2.0) + (other.width / 2.0)
        actual_distance = utils.distance(self.position, other.position)

        proximity = actual_distance <= collision_distance

        return proximity

    def handle_collision(self, other):
        pass

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.rotation += self.rotation_speed * dt
        self.rotation = utils.normalize_degrees(self.rotation)

    def __str__(self):
        form = "%s named '%s': p:(%.2f, %.2f) v:(%.2f, %.2f), r:%.2f, dr:%.2f"
        fields = (type(self).__name__, self.name, self.x, self.y,
                  self.velocity_x, self.velocity_y, self.rotation,
                  self.rotation_speed)

        return form.format(fields)
