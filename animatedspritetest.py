import pyglet
from game.animated_sprite import AnimatedSprite
from game import resources


def update(dt):
    # update each object
    for obj in game_objects:
        obj.update(dt)


if __name__ == '__main__':
    window = pyglet.window.Window(600, 500)
    batch = pyglet.graphics.Batch()

    map_specification = [
        {'name': 'idle', 'frames': 10, 'fps': 30},
        {'name': 'attack', 'frames': 10, 'fps': 30},
        {'name': 'walk', 'frames': 10, 'fps': 30},
        {'name': 'hurt', 'frames': 10, 'fps': 30}
    ]

    sprite = AnimatedSprite(frame_map=resources.circle_sprite_map,
                            frame_width=50, frame_height=50,
                            map_spec=map_specification,
                            initial_animation='idle',
                            x=300, y=250, batch=batch)

    game_objects = [sprite]

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
