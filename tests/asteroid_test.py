from game.asteroid import Asteroid
from tests.physicalobjects_test import Collider

from game import resources


def assert_in_range(value, minimum, maximum):
    if minimum > maximum:
        temp = maximum
        minimum = maximum
        minimum = temp

    assert value >= minimum and value <= maximum


def test_init():
    sut = Asteroid(name="Asteroid", img=resources.asteroid_image)

    assert sut is not None


def test_handle_collision__full_size():
    sut = Asteroid(name="Asteroid", img=resources.asteroid_image, x=5.0, y=5.0)
    collider = Collider(x=5.0, y=5.0)

    sut.handle_collision(collider)

    assert sut.dead
    assert_in_range(len(sut.new_objects), 2, 3)
    for obj in sut.new_objects:
        assert obj.scale == 0.5


def test_handle_collision__quarter_size():
    sut = Asteroid(name="Asteroid", img=resources.asteroid_image, x=5.0, y=5.0)
    sut.scale = 0.25
    collider = Collider(x=5.0, y=5.0)

    sut.handle_collision(collider)

    assert sut.dead
    assert len(sut.new_objects) == 0
