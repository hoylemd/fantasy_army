import pyglet
from game import load
from settings import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TOPBAR_VERTICAL_OFFSET,
    WINDOW_HORIZONTAL_CENTER)


game_window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(
    text="Score: 0", x=10, y=TOPBAR_VERTICAL_OFFSET, batch=main_batch)
level_label = pyglet.text.Label(
    text="Pysteroids", x=WINDOW_HORIZONTAL_CENTER, y=TOPBAR_VERTICAL_OFFSET,
    anchor_x='center', batch=main_batch)

player_ship = load.player_ship(main_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)

lives = load.player_lives(3, main_batch)

game_objects = [player_ship] + asteroids

game_window.push_handlers(player_ship)
game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    new_objects = []

    # check collisions
    total_objects = len(game_objects)
    for first_index in xrange(total_objects):
        for second_index in xrange(first_index + 1, total_objects):
            first_object = game_objects[first_index]
            second_object = game_objects[second_index]

            if not (first_object.dead or second_object.dead):
                if first_object.collides_with(second_object):
                    first_object.handle_collision(second_object)
                    second_object.handle_collision(first_object)

    # update each object
    for obj in game_objects:
        obj.update(dt)
        if obj.new_objects:
            new_objects.extend(obj.new_objects)
            obj.new_objects = []
    # remove dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_remove.delete()
        game_objects.remove(to_remove)

    # add new objects
    game_objects.extend(new_objects)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
