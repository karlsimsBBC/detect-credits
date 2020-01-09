import unittest

from detect_credits.reader import VideoReader

class TestReader(unittest.TestCase):

    path = './data/episodes/m000bqkv.mp4'

    def test_read_hashes(self):
        with VideoReader(self.path) as reader:
            video = reader.read_video()
        expeted_len = 1500
        expected_shape = (64,)
        expected_fps = 25
        expected_mode = 'bit-array'
        self.assertEqual(len(video), expeted_len)
        self.assertEqual(video.shape, expected_shape)
        self.assertEqual(video.fps, expected_fps)
        self.assertEqual(video.mode, expected_mode)

    

