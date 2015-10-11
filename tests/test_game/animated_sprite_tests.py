from mock import MagicMock
from game.animated_sprite import Animation
from tests.utils import fps_to_s


class MockImage(object):
    def __init__(self):
        self.get_region = MagicMock()


def test_animation_init__set_default_values():
    frame_map = MockImage()
    spec = {'name': 'first', 'frames': 5}

    sut = Animation(spec=spec, frame_map=frame_map, row=0, width=20, height=30)

    assert sut.name == 'first'

    assert sut.width == 20
    assert sut.height == 30

    assert len(sut.frames) == 5
    frame_map.get_region.assert_any_call(x=0, y=0, width=20, height=30)
    frame_map.get_region.assert_any_call(x=20, y=0, width=20, height=30)
    frame_map.get_region.assert_any_call(x=40, y=0, width=20, height=30)
    frame_map.get_region.assert_any_call(x=60, y=0, width=20, height=30)
    frame_map.get_region.assert_any_call(x=80, y=0, width=20, height=30)

    assert sut.fps == 30.0
    assert sut.frame_duration == fps_to_s(30.0)
    assert sut.frame_index == 0
    assert sut.since_last_frame == 0.0
