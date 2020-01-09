import unittest

from detect_credits.reader import VideoReader
from detect_credits.video import Video

class TestReader(unittest.TestCase):

    path = 'data/episodes/m000bqkv.mp4'

    def test_read_hashes(self):
        with VideoReader(self.path) as reader:
            video = reader.read_video(mode='bit-array')
        expeted_len = 1500
        expected_shape = (64,)
        expected_fps = 25
        expected_mode = 'bit-array'
        self.assertEqual(len(video), expeted_len)
        self.assertEqual(video.shape, expected_shape)
        self.assertEqual(video.fps, expected_fps)
        self.assertEqual(video.mode, expected_mode)

    def test_read_frames(self):
        with VideoReader(self.path) as reader:
            video = reader.read_video(mode='matrix')
        expeted_len = 1500
        expected_shape = (56, 100)
        expected_fps = 25
        expected_mode = 'matrix'
        self.assertEqual(len(video), expeted_len)
        self.assertEqual(video.shape, expected_shape)
        self.assertEqual(video.fps, expected_fps)
        self.assertEqual(video.mode, expected_mode)

    

