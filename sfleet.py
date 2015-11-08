import pyglet
from sfleet.sfleetgame import SfleetGame


if __name__ == '__main__':
    game = SfleetGame()

    @game.window.event
    def on_draw():
        game.window.clear()
        game.main_batch.draw()

    pyglet.clock.schedule_interval(game.update, 1/120.0)
    pyglet.app.run()
