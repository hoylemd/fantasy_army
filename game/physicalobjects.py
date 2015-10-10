import pyglet
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
import game.utils as utils


class InertialObject(pyglet.sprite.Sprite):

    def __init__(self, name="", vulnerable=False, damaging=False,
                 *args, **kwargs):
        super(InertialObject, self).__init__(*args, **kwargs)

        self.name = name
        self.dead = False
        self.vulnerable = vulnerable
        self.damaging = damaging
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.rotation_speed = 0.0

        self.new_objects = []

    def loop_position(self):
        x_min_margin = - self.image.width / 2.0
        y_min_margin = - self.image.height / 2.0
        x_max_margin = WINDOW_WIDTH - x_min_margin
        y_max_margin = WINDOW_HEIGHT - y_min_margin

        if self.x < x_min_margin:
            self.x = x_max_margin
        elif self.x > x_max_margin:
            self.x = x_min_margin

        if self.y < y_min_margin:
            self.y = y_max_margin
        elif self.y > y_max_margin:
            self.y = y_min_margin

    def die(self, dt=0.0):
        self.dead = True

    def collides_with(self, other):
        collision_distance = (self.width / 2.0) + (other.width / 2.0)
        actual_distance = utils.distance(self.position, other.position)

        proximity = actual_distance <= collision_distance

        damaged = self.vulnerable and other.damaging

        return (proximity and damaged)

    def handle_collision(self, other):
        if type(other) != type(self):
            self.die()

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.rotation += self.rotation_speed * dt
        self.rotation = utils.normalize_degrees(self.rotation)

        self.loop_position()

    def __str__(self):
        form = "%s named '%s': p:(%.2f, %.2f) v:(%.2f, %.2f), r:%.2f, dr:%.2f"
        fields = (type(self).__name__, self.name, self.x, self.y,
                  self.velocity_x, self.velocity_y, self.rotation,
                  self.rotation_speed)

        return form.format(fields)
