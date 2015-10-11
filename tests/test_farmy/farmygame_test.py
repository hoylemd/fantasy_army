from mock import MagicMock, patch
from farmy.farmygame import FarmyGame


class MockGameObject(object):
    def __init__(self, dead=False):
        self.update = MagicMock()
        self.delete = MagicMock()
        self.new_objects = []
        self.dead = dead


@patch('pyglet.window.Window')
def test_farmygame_init(mock_window):
    sut = FarmyGame()

    assert sut.window is not None
    assert sut.main_batch is not None
    assert len(sut.game_objects)
    assert mock_window.called


@patch('pyglet.window.Window')
def test_farmygame_update__updates_objects(mock_window):
    sut = FarmyGame()
    first_obj = MockGameObject()
    second_obj = MockGameObject()
    sut.game_objects.append(first_obj)
    sut.game_objects.append(second_obj)

    sut.update(0.34)

    first_obj.update.assert_called_once_with(0.34)
    second_obj.update.assert_called_once_with(0.34)


@patch('pyglet.window.Window')
def test_farmygame_update__removes_dead(mock_window):
    sut = FarmyGame()
    first_obj = MockGameObject()
    second_obj = MockGameObject(dead=True)
    sut.game_objects.append(first_obj)
    sut.game_objects.append(second_obj)

    assert len(sut.game_objects) == 3

    sut.update(0.34)

    assert len(sut.game_objects) == 2
    assert second_obj not in sut.game_objects
    assert second_obj.delete.called
