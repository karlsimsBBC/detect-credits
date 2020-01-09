import unittest

from detect_credits.dataset import Dataset

class TestDataset(unittest.TestCase):

    def test_load(self):
        data = Dataset('data/episodes')
        
        # episodes, frames per episode, points per frame
        expected_shape = (6, 1500, 64)
        self.assertEqual(data.episodes.shape, expected_shape)

        expected_fps = 25
        self.assertTrue(all(fps == expected_fps for fps in data.fps))
        
        expected_paths = [
            'data/episodes/m000c6nt.mp4', 
            'data/episodes/m000byty.mp4', 
            'data/episodes/m000cxhn.mp4', 
            'data/episodes/m000c6qs.mp4', 
            'data/episodes/m000bqkv.mp4', 
            'data/episodes/m000c6jx.mp4'
        ]
        self.assertEqual(data.paths, expected_paths)