from difflib import SequenceMatcher

import numpy as np
from sklearn.neighbors import DistanceMetric
from sklearn.cluster import KMeans


class SequenceFinder(object):

    def find(self, names, episodes, fps):
        offsets = self.frame_offsets(episodes)
        aligned_intros = self.align(episodes, offsets)
        X = self.similarity(aligned_intros)
        (start, end) = self.find_peaks(X)
        return [[(start + d) / fps, (end + d) / fps] for d in offsets]

    def find_peaks(self, X):
        threshold = self.decision_boundary(X)
        start = peak_index(min, X, threshold)
        end = peak_index(max, X, threshold)
        return (start, end)

    def peak_index(self, function, ep, threshold):
        return function(i for i, v in enumerate(ep) if v > threshold)

    def decision_boundary(self, similarities):
        X = similarities.reshape(-1, 1)
        k_means = KMeans(n_clusters=2, random_state=0).fit(X)
        return k_means.cluster_centers_[:, 0].mean()

    def similarity(self, episodes):
        # https://en.wikipedia.org/wiki/Hamming_distance
        dist = []
        hamming = DistanceMetric.get_metric('hamming')
        m = len(episodes[0])
        for i in range(m):
            x = 1 - hamming.pairwise(episodes[:, i]).mean()
            dist.append(x)
        return np.array(dist)

    def align(self, episodes, offsets):
        return [np.roll(ep, z, axis=0) for (ep, z) in zip(episodes, offsets)]

    def apply_offsets(self, start, end, offsets, fps):
        return [[(start + d) / fps, (end + d) / fps] for d in offsets]

    def find_offsets(self, episodes):
        offsets = [0]
        base = episodes[0]
        for i in range(1, len(episodes)):
            seq = SequenceMatcher(a=base, b=episodes[i])
            matches = seq.get_matching_blocks()
            diffs = np.array([m.a - m.b for m in matches if m.size > 0])
            offsets.append(diffs.mean())
        return offsets