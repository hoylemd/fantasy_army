import pyglet
from game.animated_sprite import AnimatedSprite
from farmy import resources


def update(dt):

    # update each object
    for obj in game_objects:
        obj.update(dt)


if __name__ == '__main__':
    window = pyglet.window.Window(600, 500)
    batch = pyglet.graphics.Batch()

    sprite = AnimatedSprite(img=resources.player_image, x=300, y=250, batch=batch)

    game_objects = [sprite]

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
