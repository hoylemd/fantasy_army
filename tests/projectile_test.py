from mock import patch
from game.projectile import Projectile
from game import resources


def test_init():
    sut = Projectile(name="bullet", img=resources.bullet_image,
                     x=100.0, y=200.0)

    assert sut is not None
    assert sut.x == 100.0
    assert sut.y == 200.0


@patch('game.projectile.clock')
def test_init__dies_after_default_time(mock_clock):
    sut = Projectile(name="bullet", img=resources.bullet_image,
                     x=100.0, y=200.0)

    mock_clock.schedule_once.assert_called_with(sut.die, 0.5)


@patch('game.projectile.clock')
def test_init__dies_after_set_time(mock_clock):
    sut = Projectile(name="bullet", img=resources.bullet_image,
                     x=100.0, y=200.0, lifespan=1.25)

    mock_clock.schedule_once.assert_called_with(sut.die, 1.25)
