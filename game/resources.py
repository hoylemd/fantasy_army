import pyglet
pyglet.resource.path = ['resources', '../../resources']
pyglet.resource.reindex()


def center_image(image):
    """Sets an image's anchor point to it's center"""
    image.anchor_x = image.width / 2.0
    image.anchor_y = image.height / 2.0

chevron_image = pyglet.resource.image('chevron.png')
bullet_image = pyglet.resource.image('bullet.png')
asteroid_image = pyglet.resource.image('asteroid.png')
engineflame_image = pyglet.resource.image('engineflame.png')

center_image(chevron_image)
center_image(bullet_image)
center_image(asteroid_image)

engineflame_image.anchor_x = engineflame_image.width / 2.0
engineflame_image.anchor_y = engineflame_image.height * 2.0
