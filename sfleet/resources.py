import pyglet
pyglet.resource.path = ['resources', '../../resources']
pyglet.resource.reindex()


def center_image(image):
    """Sets an image's anchor point to it's center"""
    image.anchor_x = image.width / 2.0
    image.anchor_y = image.height / 2.0

arkadian_cruiser_image = pyglet.resource.image('arkadian_cruiser.png')
terran_cruiser_image = pyglet.resource.image('terran_cruiser.png')
bullet_image = pyglet.resource.image('bullet.png')

center_image(bullet_image)
center_image(arkadian_cruiser_image)
center_image(terran_cruiser_image)
