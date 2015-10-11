from pyglet.sprite import Sprite


class AnimatedSprite(Sprite):
    def __init__(self, *args, **kwargs):
        super(AnimatedSprite, self).__init__(*args, **kwargs)

    def update(self, dt):
        pass
