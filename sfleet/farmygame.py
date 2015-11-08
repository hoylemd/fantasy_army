import pyglet
import resources
from hero import Hero


class FarmyGame(object):
    def __init__(self, fullscreen=True):
        self.window = pyglet.window.Window(fullscreen=fullscreen)
        self.main_batch = pyglet.graphics.Batch()

        player_hero = self.load_player_hero()
        self.player_hero = player_hero

        self.game_objects = [player_hero]

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

    def load_player_hero(self, batch=None):
        if batch is None:
            batch = self.main_batch

        player_hero = Hero(name="Player Hero",
                           x=self.window.width / 2.0,
                           y=self.window.height / 2.0,
                           body_image=resources.player_image,
                           batch=batch)

        self.window.push_handlers(player_hero)
        self.window.push_handlers(player_hero.key_handler)
        return player_hero
