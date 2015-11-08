import pyglet
from farmy.farmygame import FarmyGame


if __name__ == '__main__':
    game = FarmyGame()

    @game.window.event
    def on_draw():
        game.window.clear()
        game.main_batch.draw()

    pyglet.clock.schedule_interval(game.update, 1/120.0)
    pyglet.app.run()
