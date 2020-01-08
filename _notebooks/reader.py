import os

import cv2


class VideoReader(object):

    def __init__(self, inpath, mono=True):
        self.inpath = inpath
        self.mono = mono

    def read_frames(self):
        frames = []
        while self.capture.isOpened():
            result, frame = self.capture.read()
            if not result:
                break
            if self.mono:
                # convert to grayscale if mono
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame)
        return frames

    def read_hashes(self):
        hashes = []
        while self.capture.isOpened():
            result, frame = self.capture.read()
            if not result:
                break
            if self.mono:
                # convert to grayscale if mono
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hashes.append(self.dhash(frame))
        return hashes

    def dhash(self, image, hash_size=8):
        # resize the input image, adding a single column (width) so we
        # can compute the horizontal gradient
        resized = cv2.resize(image, (hash_size + 1, hash_size))
        # compute the (relative) horizontal gradient between adjacent
        # column pixels
        diff = resized[:, 1:] > resized[:, :-1]
        # convert the difference image to a hash
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

    def __enter__(self):
        self._set_capture(self.inpath)
        if not self.capture.isOpened():
            print("Error opening video file")
            return None
        return self

    def __exit__(self, _type, value, traceback):
        self.capture.release()
        if any([_type, value, traceback]):
            print('ERROR')
            print(f'exit: {_type}, {value}, {traceback}')

    def _set_capture(self, path):
        self.capture = cv2.VideoCapture(path)
        self.FPS = self.capture.get(cv2.CAP_PROP_FPS)