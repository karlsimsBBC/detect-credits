import cv2

from detect_credits import video


class VideoReader(object):

    def __init__(self, path):
        self.path = path

    def read_video(self, mode=video.BIT_ARRAY_MODE):
        if mode == video.MATRIX_MODE:
            frames = self.read_frames()
        elif mode == video.BIT_ARRAY_MODE:
            frames = self.read_hashes()
        return video.Video(self.path, frames, self.FPS, mode)

    def read_frames(self):
        frames = []
        while self.capture.isOpened():
            result, frame = self.capture.read()
            if not result:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame)
        return frames

    def read_hashes(self):
        return [self.dhash(frame) for frame in self.read_frames()]

    def dhash(self, image, hash_size=8):
        resized = cv2.resize(image, (hash_size + 1, hash_size))
        diff = resized[:, 1:] > resized[:, :-1]
        return diff.flatten()

    def dhash2(self, image, hash_size=8):
        frames = self.dhash(image, hash_size=hash_size)
        return sum([2 ** i for (i, v) in enumerate(frames) if v])

    def __enter__(self):
        self.capture = cv2.VideoCapture(self.path)
        self.FPS = self.capture.get(cv2.CAP_PROP_FPS)
        if not self.capture.isOpened():
            raise FileNotFoundError('Could not find file %s' % self.path)
        return self

    def __exit__(self, _type, value, traceback):
        self.capture.release()
        if any([_type, value, traceback]):
            raise _type(value, traceback)