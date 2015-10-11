from mock import MagicMock
from game.animated_sprite import Animation
from tests.utils import fps_to_s


class MockImage(object):
    def __init__(self):
        self.get_region = MagicMock()


class RegionBounceImage(object):
    def get_region(self, x=0.0, y=0.0, width=0.0, height=0.0):
        return "(%.2f, %.2f)&%.2fx%.2f" % (x, y, width, height)


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


def test_animation_init__fps_optional():
    frame_map = MockImage()
    spec = {'name': 'first', 'frames': 5, 'fps': 17.5}

    sut = Animation(spec=spec, frame_map=frame_map, row=0, width=20, height=30)

    assert sut.fps == 17.5
    assert sut.frame_duration == fps_to_s(17.5)


def test_animation_init__valueerror_on_missing_args():
    try:
        Animation(row=0, width=20, height=30)
        assert False
    except ValueError as err:
        assert err.message == 'must pass in arguments'

    frame_map = MockImage()
    spec = {'name': 'first', 'frames': 5, 'fps': 17.5}
    try:
        Animation(spec=spec, frame_map=frame_map)
        assert False
    except ValueError as err:
        assert err.message == 'must pass in arguments'


def test_animation_init__valueerror_on_missing_spec_keys():
    frame_map = MockImage()
    spec = {}
    try:
        Animation(spec=spec, frame_map=frame_map, row=0, width=50.0, height=50.0)
        assert False
    except ValueError as err:
        assert err.message == 'keys missing from spec'


def test_animation_update__no_frame_change():
    frame_map = RegionBounceImage()
    spec = {'name': 'first', 'frames': 5}

    sut = Animation(spec=spec, frame_map=frame_map, row=0, width=20, height=30)
    dt = fps_to_s(30.0) - 0.025
    first_frame = sut.image

    sut.update(dt)

    assert sut.since_last_frame == dt
    assert sut.image is first_frame


def test_animation_update__advances_frame():
    frame_map = RegionBounceImage()
    spec = {'name': 'first', 'frames': 5}

    sut = Animation(spec=spec, frame_map=frame_map, row=0, width=20, height=30)
    dt = fps_to_s(30.0) + 0.025
    first_frame = sut.image

    sut.update(dt)

    assert sut.since_last_frame == (dt - fps_to_s(30.0))
    assert sut.image is not first_frame


def test_animation_update__loops_frame():
    pass


def test_animation_update__fps_affects_update_rate():
    pass
