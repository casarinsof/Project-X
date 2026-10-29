"""
Reference https://towardsdatascience.com/using-fastai-to-classify-japanese-kanji-characters-47d7edd4d569
Dataset divided into train and test and resampled following the guideline of Ref.
Dataset availabel in https://github.com/rois-codh/kmnist
Video Generation : https://gist.github.com/praateekmahajan/b42ef0d295f528c986e2b3a0b31ec1fe?msclkid=68bf356eb00611ec860ddfaf07fbbb14
"""

from collections import OrderedDict
from sklearn.model_selection import train_test_split
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random
from scipy import ndimage


class FrameGenerator(object):
    def __call__(self, image):
        if not isinstance(image, np.ndarray):
            image = np.array(image)
        video = [image]  # In this way I'm sure the first frame is the seed that generated the video
        frames = [8, 16, 24, 32]
        angles = [45, 30, 10, 6]

        f_x = random.choice(frames)
        f_y = random.choice(frames)
        alpha = random.choice(angles)
        video_x = [np.roll(image, round(image.shape[0] / f_x) * i, axis=0) for i in range(f_x)]
        video_y = [np.roll(image, round(image.shape[1] / f_y) * i, axis=1) for i in range(f_y)]
        video_rot = []
        for i in range(round(180 / alpha)):
            img = ndimage.rotate(image, alpha*(i+1), reshape=False)
            video_rot.append(img)

        augm = [video_x, video_y, video_rot]
        a = random.choice(augm)
        video.extend(a)
        return video


def video_creation(dest, filename_out, x, y):
    gen = FrameGenerator()
    class_dict = OrderedDict()
    output = []
    for cl in np.unique(y):
        class_dict[cl] = np.where(y == cl)

    for i in class_dict:
        seeds = x[class_dict[i]]
        all_videos = [gen(s) for s in seeds]
        for idx, video in enumerate(all_videos):
            output.append('%s %d %d' % ('{}/frames/{}_video_class{}_{:05d}'.format(filename_out, filename_out, i, idx), len(video), i))
            des_dir = os.path.join(dest, 'frames', '{}_video_class{}_{:05d}'.format(filename_out, i, idx))
            if not os.path.exists(des_dir):
                os.makedirs(des_dir)
            for fidx, frame in enumerate(video):
                im = Image.fromarray(np.array(frame))
                im.save(des_dir + '/frames_{:05d}.jpg'.format(fidx + 1))
    with open(os.path.join(dest, '{}_videofolder.txt'.format(filename_out)),'w') as f:
        f.write('\n'.join(output))
    return


def load(f):
    return np.load(f, allow_pickle=True)['arr_0']


if __name__ == '__main__':
    X_train = load('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-train-imgs.npz')
    y_train = load('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-train-labels.npz')
    X_test = load('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-test-imgs.npz')
    y_test = load('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-test-labels.npz')

    print(f"train_image:\t{X_train.shape}")
    print(f"train_label:\t{y_train.shape}")
    print(f"Unique Kanji characters (Training): {len(np.unique(y_train))}")
    print(f"Unique Kanji characters (Test): {len(np.unique(y_test))}")

    dir = '/m100_work/IscrB_SRL4V/cugwu/data/complex_kanji/train'
    file = 'train'
    video_creation(dir, file,  X_train, y_train)

    dir = '/m100_work/IscrB_SRL4V/cugwu/data/complex_kanji/val'
    file = 'val'
    video_creation(dir, file,  X_test, y_test)
    print('\nVideo creation finished')





