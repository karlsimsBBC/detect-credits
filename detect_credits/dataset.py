import os
import numpy as np

from detect_credits.reader import VideoReader


class Dataset(object):

    def __init__(self, root, video_reader=VideoReader, fps=None):
        self.paths = []
        self.episodes = []
        self.fps = []
        for path in self.video_paths(root):
            with video_reader(path) as reader:
                self.fps.append(reader.FPS)
                self.episodes.append(reader.read_hashes())
            self.paths.append(path)
        self.episodes = np.array(self.episodes)

    def video_paths(self, root):
        for name in os.listdir(root):
            if name.startswith('.'):
                continue
            yield os.path.join(root, name)
    