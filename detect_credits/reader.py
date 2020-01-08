import cv2

from skipintro.video import Video


class VideoReader(object):

    def __init__(self, path):
        self.path = path

    def read_frames(self):
        frames = []
        while self.capture.isOpened():
            result, frame = self.capture.read()
            if not result:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame)
        return Video(self.path, frames, self.FPS)

    def read_hashes(self):
        hashes = []
        while self.capture.isOpened():
            result, frame = self.capture.read()
            if not result:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hashes.append(self.dhash(frame))
        return HashedVideo(self.path, hashes, self.FPS)

    def dhash(self, image, hash_size=8):
        resized = cv2.resize(image, (hash_size + 1, hash_size))
        diff = resized[:, 1:] > resized[:, :-1]
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

    def __enter__(self):
        self.capture = cv2.VideoCapture(self.path)
        self.FPS = self.capture.get(cv2.CAP_PROP_FPS)
        if not self.capture.isOpened():
            print("Error opening video file")
            return None
        return self

    def __exit__(self, _type, value, traceback):
        self.capture.release()
        if any([_type, value, traceback]):
            print('ERROR')
            print(f'exit: {_type}, {value}, {traceback}')