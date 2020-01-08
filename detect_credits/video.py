

class Video(object):

    def __init__(self, name, frames, fps):
        self.name = name
        self.fps = fps
        self.frames = frames

    # def dhash(self, image, hash_size=8):
    #     resized = cv2.resize(image, (hash_size + 1, hash_size))
    #     diff = resized[:, 1:] > resized[:, :-1]
    #     return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
