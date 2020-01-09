import os
import math
import cv2
import numpy as np

import matplotlib.pyplot as plt

from reader import VideoReader

def load_episodes(base='./data/episodes'):
    videos = []
    for path in videopaths(base):
        with VideoReader(path) as vf:
            videos.append(vf.read_frames())
    return videos

def load_hashes(base='./data/episodes'):
    videos = []
    for path in videopaths(base):
        with VideoReader(path) as vf:
            videos.append(vf.read_hashes())
    return videos

def videopaths(base):
    for name in os.listdir(base):
        if name.startswith('.'):
            continue
        yield os.path.join(base, name)

def show_similarity(X):
    plt.rcParams["figure.figsize"] = [14,4]
    plt.plot(np.arange(0, len(X)), X)
    plt.show()

def show_mean_similarity(X, names):
    size = len(X)
    cols = 3
    rows = math.ceil(size / cols)
    plt.rcParams["figure.figsize"] = [16, rows*3.25]
    fig, axs = plt.subplots(rows, cols)
    for i, ep in enumerate(X):
        ax = axs[i//3, i%3]
        ax.plot(np.arange(0, len(ep)), ep)
        ax.set_title(names[i])
        ax.set_yticks(np.arange(0.8, 1.05, step=0.05))
    plt.show()

def show_frames(episode, intro=None, colors=['bone', 'autumn']):
    fps = 25
    if intro:
        start_frame = int(intro['start'] * fps)
        end_frame = int(intro['end'] * fps)
        classes = set(range(start_frame, end_frame))
    else:
        classes = set()
    num_imgs = len(episode) // fps
    columns = 10
    rows = num_imgs // columns + 1
    fig = plt.figure(figsize=(18, rows+rows//3))
    for i in range(columns*rows):
        if i * fps >= len(episode):
            continue
        img = episode[i*fps]
        ax = fig.add_subplot(rows, columns, i+1)
        timestamp = '{:02}:{:02}:00'.format(i//60, i % 60)
        ax.set_title(timestamp)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap=colors[int(i*fps in classes)])
    plt.show()

def show_images(imgs, titles):
    fig = plt.figure(figsize=(8, 2))
    for i, (img, title) in enumerate(zip(imgs, titles)):
        ax = fig.add_subplot(1, len(imgs), i+1)
        ax.set_title(title)
        plt.axis('off')
        plt.imshow(img, cmap='bone')
    plt.show()