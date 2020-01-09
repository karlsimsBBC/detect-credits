import os
import numpy as np

import matplotlib.pyplot as plt

root = 'test/graphs'

def save_graph(X, name):
    plt.plot(np.arange(0, len(X)), X)
    prev_name = os.path.join(root, f'{name}_prev.png')
    latest_name = os.path.join(root, f'{name}_latest.png')
    if os.path.exists(latest_name):
        os.rename(latest_name, prev_name)
    plt.savefig(latest_name)

def show_frames(episode, intro=None, colors=['gray', 'pink']):
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
