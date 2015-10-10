from farmy import load


def test_player_hero():
    sut = load.player_hero()

    assert sut.speed == 10
