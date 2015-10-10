from game import load, utils
from settings import WINDOW_HORIZONTAL_CENTER, WINDOW_VERTICAL_CENTER


def test_asteroids__3():
    suts = load.asteroids(3, (100, 100))

    assert len(suts) == 3


def test_asteroids__20_no_collosions():
    suts = load.asteroids(3, (100, 100))

    for sut in suts:
        assert utils.distance(sut.position, (100, 100)) >= 100


def test_player_ship():
    sut = load.player_ship()

    assert sut.thrust == 200.0
    assert sut.maneuvering_thrust == 360.0

    assert sut.weapon_projectile_speed == 700.0

    assert sut.x == WINDOW_HORIZONTAL_CENTER
    assert sut.y == WINDOW_VERTICAL_CENTER

    assert sut.center_x == WINDOW_HORIZONTAL_CENTER
    assert sut.center_y == WINDOW_VERTICAL_CENTER
