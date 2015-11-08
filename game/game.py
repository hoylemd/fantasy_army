import pyglet


class Game(object):
    def __init__(self, fullscreen=True):
        self.window = pyglet.window.Window(fullscreen=fullscreen)
        self.main_batch = pyglet.graphics.Batch()
        self.game_objects = []

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
