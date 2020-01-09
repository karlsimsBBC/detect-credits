import os
import unittest

from detect_credits.detect import SequenceFinder
from detect_credits.dataset import Dataset

from detect_credits.reader import VideoReader

from test.utils import save_graph
from test.utils import show_frames


class TestSequenceFinder(unittest.TestCase):
    
    data = Dataset('./data/episodes')
    
    finder = SequenceFinder()

    def test_find(self):
        mixed = Dataset('./data/mixed')
        episodes = load_frames('./data/mixed')
        result = self.finder.find(mixed.episodes, mixed.fps)
        for (start, end), ep in zip(result, episodes):
            show_frames(ep, {'start': start, 'end': end})
    
    def test_find_offsets(self):
        offsets = self.finder.find_offsets(self.data.episodes)
        print(offsets)

    def test_similarity(self):
        result = self.finder.similarity(self.data.episodes)
        expected_len = 1500
        # right length
        self.assertEqual(len(result), expected_len)
        # all between 0 and 1
        self.assertTrue(all(0 <= i <= 1 for i in result))
        save_graph(result, 'similarities')

    def test_discriminate(self):
        X = self.finder.similarity(self.data.episodes)
        result = self.finder.discriminate(X)
        expected = (0.0, 621)
        self.assertEqual(result, expected)
        




        
def load_frames(base='./data/episodes'):
    videos = []
    for path in videopaths(base):
        with VideoReader(path) as vf:
            videos.append(vf.read_frames())
    return videos

def videopaths(base):
    for name in os.listdir(base):
        if name.startswith('.'):
            continue
        yield os.path.join(base, name)
        

