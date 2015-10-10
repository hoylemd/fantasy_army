from farmy.hero import Hero
from farmy import resources


def test_init__initial_values():
    sut = Hero(body_image=resources.player_image)

    assert sut.speed == 10

    assert sut.x == 0.0
    assert sut.y == 0.0

    assert sut.center_x == 0.0
    assert sut.center_y == 0.0


def test_init__specified_values():
    sut = Hero(body_image=resources.player_image, x=123.4, y=421.54, speed=10)

    assert sut.speed == 10

    assert sut.x == 123.4
    assert sut.y == 421.54

    assert sut.center_x == 123.4
    assert sut.center_y == 421.54


def set_up_hero():
    return Hero(body_image=resources.player_image, x=200.0, y=300.0, speed=10)
