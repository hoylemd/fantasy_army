import pyglet
import resources
from vessel import Vessel


class SfleetGame(object):
    def __init__(self, fullscreen=True):
        self.window = pyglet.window.Window(fullscreen=fullscreen)
        self.main_batch = pyglet.graphics.Batch()

        self.player_fleet = self.load_player_fleet()
        self.enemy_fleet = self.load_enemy_fleet()

        self.game_objects = self.player_fleet + self.enemy_fleet

    def update(self, dt):
        new_objects = []

        # update each object
        for obj in self.game_objects:
            obj.update(dt)
            if obj.new_objects:
                new_objects.extend(obj.new_objects)
                obj.new_objects = []

        # remove dead objects
        for to_remove in [obj for obj in self.game_objects if obj.dead]:
            to_remove.delete()
            self.game_objects.remove(to_remove)

        # add new objects
        self.game_objects.extend(new_objects)

    def load_player_fleet(self, batch=None):
        if batch is None:
            batch = self.main_batch

        ship_spec = {
            'speed': 10,
            'hull': 100,
            'armour': 50,
            'armour_threshold': 10,
            'shield': 50,
            'shield_recharge': 10,
            'weapon_range': 30,
            'weapon_damage': 20
        }

        player_ship = Vessel(name="ASF Brantd",
                             x=self.window.width / 2.0,
                             y=200.0,
                             rotation=0,
                             hull_image=resources.arkadian_cruiser_image,
                             spec=ship_spec,
                             batch=batch)

        self.window.push_handlers(player_ship)
        return [player_ship]

    def load_enemy_fleet(self, batch=None):
        if batch is None:
            batch = self.main_batch

        ship_spec = {
            'speed': 10,
            'hull': 100,
            'armour': 50,
            'armour_threshold': 10,
            'shield': 50,
            'shield_recharge': 10,
            'weapon_range': 30,
            'weapon_damage': 20
        }

        enemy_ship = Vessel(name="ITV Vladimir",
                            x=self.window.width / 2.0,
                            y=self.window.height - 200.0,
                            rotation=180.0,
                            hull_image=resources.terran_cruiser_image,
                            spec=ship_spec,
                            batch=batch)

        self.window.push_handlers(enemy_ship)
        return [enemy_ship]
