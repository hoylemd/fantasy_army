from pyglet.sprite import Sprite



class Animation(object):
    """
        spec format: {'name': 'idle', 'frames': 10 (, fps: 30.0)}
    """
    def __init__(self, spec=None, frame_map=None, row=0,
                 width=None, height=None):
        if None in [spec, frame_map, width, height]:
            raise ValueError('must pass in arguments')

        if 'name' not in spec or 'frames' not in spec:
            raise ValueError('keys missing from spec')

        # book keeping
        self.name = spec['name']

        # frame information
        self.width = width
        self.height = height

        # generate the frames
        self.frames = []
        for i in range(spec['frames']):
            x = i * width
            y = row * height
            self.frames.append(
                frame_map.get_region(x=x, y=y, width=width, height=height))
        self.image = self.frames[0]

        # timing info
        self.fps = spec['fps'] if 'fps' in spec else 30.0
        self.frame_duration = 1.0 / float(self.fps)
        self.frame_index = 0
        self.since_last_frame = 0.0

    def update(self, dt):
        # time since last frame update
        since_last_frame = self.since_last_frame + dt

        # number of frames to advance by
        frames_passed = int(since_last_frame / self.frame_duration)
        if frames_passed:
            frame_index = (self.frame_index + frames_passed) % len(self.frames)

            # consume time
            since_last_frame -= frames_passed * self.frame_duration

            self.frame_index = frame_index
            self.image = self.frames[frame_index]

        # set the state
        self.since_last_frame = since_last_frame


class AnimatedSprite(Sprite):
    def __init__(self, frame_map=None, frame_width=None, frame_height=None,
                 map_spec=None, initial_animation='default', *args, **kwargs):
        if None in [frame_map, frame_width, frame_height, map_spec]:
            raise ValueError('must pass in frames and dimensions')

        # save the frame information
        self.frame_width = frame_width
        self.frame_height = frame_height

        # save the spec
        self.map_spec = map_spec

        # create the animations hash
        self.animations = {}
        i = 0
        for spec in map_spec:
            # create this animation
            anim = Animation(
                spec=spec, frame_map=frame_map, row=i,
                width=frame_width, height=frame_height)
            self.animations[anim.name] = anim
            i += 1

        # initialize the first animation
        self.current_animation = self.animations[initial_animation]

        self.update(0.0)

        super(AnimatedSprite, self).__init__(img=self.img, *args, **kwargs)

    def update(self, dt):
        self.current_animation.update(dt)
        self.img = self.current_animation.image
