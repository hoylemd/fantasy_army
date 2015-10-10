import math
from pyglet.sprite import Sprite
from pyglet.window import key
from physicalobjects import InertialObject
from projectile import Projectile


class Player(InertialObject):
    def __init__(self, name="", hull_image=None, engine_image=None,
                 x=0.0, y=0.0, thrust=200.0, maneuvering_thrust=360.0,
                 weapon_projectile_image=None, weapon_projectile_speed=700.0,
                 *args, **kwargs):

        super(Player, self).__init__(img=hull_image, name=name,
                                     vulnerable=True, x=x, y=y,
                                     *args, **kwargs)

        self.engineflame = Sprite(img=engine_image, x=x, y=y, *args, **kwargs)
        self.engineflame.visible = False

        self.thrust = thrust
        self.maneuvering_thrust = maneuvering_thrust

        self.weapon_projectile_image = weapon_projectile_image
        self.weapon_projectile_speed = weapon_projectile_speed

        self.center_x = x
        self.center_y = y

        self.key_handler = key.KeyStateHandler()

    def fire(self):
        angle_radians = math.radians(self.rotation)
        ship_radius = self.image.width/2 + 5.0
        bullet_x = self.x + math.sin(angle_radians) * ship_radius
        bullet_y = self.y + (math.cos(angle_radians) * ship_radius)
        new_bullet = Projectile(name="bullet",
                                img=self.weapon_projectile_image,
                                x=bullet_x, y=bullet_y, batch=self.batch)
        new_bullet.velocity_x = (
            self.velocity_x +
            math.sin(angle_radians) * self.weapon_projectile_speed
        )
        new_bullet.velocity_y = (
            self.velocity_y +
            math.cos(angle_radians) * self.weapon_projectile_speed
        )
        self.new_objects.append(new_bullet)

    def update(self, dt):
        rotational_dv = self.maneuvering_thrust * dt
        propulsive_dv = self.thrust * dt

        modified_rot_speed = self.rotation_speed
        if self.key_handler[key.RIGHT]:
            modified_rot_speed += rotational_dv
        if self.key_handler[key.LEFT]:
            modified_rot_speed -= rotational_dv
        if self.key_handler[key.DOWN]:
            direction = 1.0
            if self.rotation_speed < 0:
                direction = -1.0
            abs_rotation = modified_rot_speed * direction
            modified_rot_speed = direction * (abs_rotation - rotational_dv)
            if (direction * modified_rot_speed) < 0:
                modified_rot_speed = 0.0
        if self.key_handler[key.SPACE]:
            self.fire()

        # interpolate accelerated rotation change
        self.rotation_speed = (modified_rot_speed + self.rotation_speed) / 2.0

        modified_vx = self.velocity_x
        modified_vy = self.velocity_y
        if self.key_handler[key.UP]:
            angle_radians = math.radians(self.rotation)
            modified_vx += math.sin(angle_radians) * propulsive_dv
            modified_vy += math.cos(angle_radians) * propulsive_dv
            self.engineflame.visible = True
        else:
            self.engineflame.visible = False

        # iterpolate accelerated velocity change
        self.velocity_x = (modified_vx + self.velocity_x) / 2.0
        self.velocity_y = (modified_vy + self.velocity_y) / 2.0

        super(Player, self).update(dt)

        # update subsprites
        self.engineflame.x = self.x
        self.engineflame.y = self.y
        self.engineflame.rotation = self.rotation

        self.rotation_speed = modified_rot_speed
        self.velocity_x = modified_vx
        self.velocity_y = modified_vy

        if self.key_handler[key.C]:
            self.x = self.center_x
            self.y = self.center_y
            self.velocity_x = 0.0
            self.velocity_y = 0.0
            self.rotation = 0.0
            self.rotation_speed = 0.0

    def delete(self):
        self.engineflame.delete()
        super(Player, self).delete()
