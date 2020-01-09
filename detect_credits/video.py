

BIT_ARRAY_MODE = 'bit-array'
MATRIX_MODE = 'matrix'

class Video(object):

    def __init__(self, name, frames, fps, mode):
        self.name = name
        self.fps = fps
        self.frames = frames
        self.mode = mode
        self.hashes = None

    def __len__(self):
        return len(self.frames)

    @property
    def shape(self):
        return self.frames[0].shape

    def hashes(self):
        if self.hashes:
            return self.hashes
        if self.mode == BIT_ARRAY_MODE:
            self.hashes = self.to_hashes(self.frames)
            return self.hashes
        raise AttributeError('cannot convert matrices into hashes')

    def to_hashes(self, frames):
        return sum([2 ** i for (i, v) in enumerate(self.frames) if v])

