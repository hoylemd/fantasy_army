from mock import MagicMock
import pyglet
from pyglet.window import key
from game.player import Player
from game import resources
from tests.scaffolding import fps_to_s, eq_within_epsilon


def test_init__initial_values():
    sut = Player(hull_image=resources.player_image,
                 engine_image=resources.engineflame_image)

    assert isinstance(sut.engineflame, pyglet.sprite.Sprite)
    assert not sut.engineflame.visible

    assert sut.thrust == 200.0
    assert sut.maneuvering_thrust == 360.0

    assert sut.weapon_projectile_speed == 700.0

    assert sut.x == 0.0
    assert sut.y == 0.0

    assert sut.center_x == 0.0
    assert sut.center_y == 0.0


def test_init__specified_values():
    sut = Player(hull_image=resources.player_image,
                 engine_image=resources.engineflame_image, x=123.4, y=421.54,
                 thrust=150.0, maneuvering_thrust=500.0,
                 weapon_projectile_speed=950.0)

    assert isinstance(sut.engineflame, pyglet.sprite.Sprite)
    assert not sut.engineflame.visible

    assert sut.thrust == 150.0
    assert sut.maneuvering_thrust == 500.0

    assert sut.weapon_projectile_speed == 950.0

    assert sut.x == 123.4
    assert sut.y == 421.54

    assert sut.center_x == 123.4
    assert sut.center_y == 421.54


def set_up_sluggish_player():
    return Player(hull_image=resources.player_image,
                  engine_image=resources.engineflame_image,
                  x=200.0, y=300.0,
                  thrust=10.0, maneuvering_thrust=15.0)


def test_init__sluggish():
    sut = set_up_sluggish_player()

    assert sut.rotation_speed == 0.0
    assert sut.rotation == 0.0
    assert sut.velocity_x == 0.0
    assert sut.velocity_y == 0.0
    assert sut.x == 200.0
    assert sut.y == 300.0


def test_update__turn_right():
    sut = set_up_sluggish_player()

    # turn right
    sut.key_handler.on_key_press(key.RIGHT, None)

    sut.update(fps_to_s(60))  # one 60 fps frame

    assert sut.rotation_speed == 0.25
    assert eq_within_epsilon(sut.rotation, 0.0021, 0.0001)

    sut.update(fps_to_s(60) * 59)  # finish this second

    sut.key_handler.on_key_release(key.RIGHT, None)

    assert sut.rotation_speed == 15.0
    assert eq_within_epsilon(sut.rotation, 7.5)

    sut.update(1.0)  # one second

    assert sut.rotation_speed == 15.0
    assert eq_within_epsilon(sut.rotation, 22.5)


def test_update__turn_left():
    sut = set_up_sluggish_player()

    # turn left
    sut.key_handler.on_key_press(key.LEFT, None)

    sut.update(fps_to_s(60) * 1.5)

    assert sut.rotation_speed == -0.375
    assert eq_within_epsilon(sut.rotation, 359.9953, 0.0001)

    sut.update(fps_to_s(60) * 58.5)  # finish this second

    sut.key_handler.on_key_release(key.LEFT, None)

    assert sut.rotation_speed == -15
    assert eq_within_epsilon(sut.rotation, 352.5)

    sut.update(1.0)  # one second

    assert sut.rotation_speed == -15
    assert eq_within_epsilon(sut.rotation, 337.5)


def test_update__SAS():
    sut = set_up_sluggish_player()

    # start turning
    sut.key_handler.on_key_press(key.RIGHT, None)

    sut.update(1.0)  # one 60 fps frame

    sut.key_handler.on_key_release(key.RIGHT, None)

    assert sut.rotation_speed == 15.0
    assert eq_within_epsilon(sut.rotation, 7.5)

    # engage SAS
    sut.key_handler.on_key_press(key.DOWN, None)

    sut.update(0.5)  # stabilize for half a second

    assert sut.rotation_speed == 7.5
    assert eq_within_epsilon(sut.rotation, 13.12)

    sut.key_handler.on_key_release(key.DOWN, None)

    sut.update(0.5)  # drift for half a second

    assert sut.rotation_speed == 7.5
    assert eq_within_epsilon(sut.rotation, 16.87)

    sut.key_handler.on_key_press(key.DOWN, None)

    sut.update(1.0)  # stabilize for a full second

    assert sut.rotation_speed == 0.0
    assert eq_within_epsilon(sut.rotation, 20.62)


def test_update__thrust():
    sut = set_up_sluggish_player()

    # artificially set rotation
    sut.rotation = 45.0

    assert sut.velocity_x == 0.0
    assert sut.velocity_y == 0.0
    assert sut.x == 200.0
    assert sut.y == 300.0

    # engage thrust
    sut.key_handler.on_key_press(key.UP, None)
    sut.update(1.0)

    assert eq_within_epsilon(sut.velocity_x, 7.08)
    assert eq_within_epsilon(sut.velocity_y, 7.08)
    assert eq_within_epsilon(sut.x, 203.54)
    assert eq_within_epsilon(sut.y, 303.54)

    # stop thrust and drift
    sut.key_handler.on_key_release(key.UP, None)
    sut.update(2.0)

    assert eq_within_epsilon(sut.velocity_x, 7.08)
    assert eq_within_epsilon(sut.velocity_y, 7.08)
    assert eq_within_epsilon(sut.x, 217.68)
    assert eq_within_epsilon(sut.y, 317.68)

    # stop altogether
    sut.rotation += 180.0
    sut.key_handler.on_key_press(key.UP, None)
    sut.update(1.0)

    assert eq_within_epsilon(sut.velocity_x, 0.0)
    assert eq_within_epsilon(sut.velocity_y, 0.0)
    assert eq_within_epsilon(sut.x, 221.22)
    assert eq_within_epsilon(sut.y, 321.22)


def test_update__thrust_shows_engineflame():
    sut = set_up_sluggish_player()

    assert sut.engineflame.visible is False

    sut.key_handler.on_key_press(key.UP, None)
    sut.update(1.0)

    assert sut.engineflame.visible is True

    sut.key_handler.on_key_release(key.UP, None)
    sut.update(1.0)

    assert sut.engineflame.visible is False


def test_key_handler__space_calls_fire():
    sut = set_up_sluggish_player()

    sut.fire = MagicMock()

    sut.key_handler.on_key_press(key.SPACE, None)
    sut.update(1.0)

    assert sut.fire.called
