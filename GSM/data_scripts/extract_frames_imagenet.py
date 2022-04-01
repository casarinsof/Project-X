# https://github.com/pytorch/examples/tree/main/imagenet

import os
import numpy as np
from PIL import Image
import random
import torchvision.datasets as datasets
from scipy import ndimage

data = '/m100_wai/DATASETS_AI/imagenet/ilsvrc2012'


class FrameGenerator(object):
    def __call__(self, image):
        if not isinstance(image, np.ndarray):
            image = np.array(image)
        video = [image]  # In this way I'm sure the first frame is the seed that generated the video
        frames = [8, 16, 24, 32]
        angles = [6, 10, 30, 45]
        for times in range(2):
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
            augm = a = random.sample(augm, k=3)
            for i in range(len(augm)):
                video.extend(a[i])
        return video


def video_creation(dest, filename_out, dataset):
    gen = FrameGenerator()
    output = []
    for keys in dataset.class_to_idx.keys():
        i = dataset.class_to_idx[keys]
        seeds = [img for (img, cl) in dataset if cl == i]  # TODO C'e' qualcosa che prende un sacco di tempo
                                                           #    nella generazione del dataset forse e' questo.
        print('....Generating videos....')
        all_videos = [gen(s) for s in seeds]
        print('Videos generated!')
        sub_videos = []
        for idx, video in enumerate(all_videos):
            sub_videos.extend(video)
            if (idx+1) % 20 == 0:
                output.append('%s %d %d' % ('{}/frames/{}_video_class{}_{:05d}'.format(filename_out,filename_out, i, idx), len(sub_videos), i))
                des_dir = os.path.join(dest, 'frames', '{}_video_class{}_{:05d}'.format(filename_out, i, idx))
                if not os.path.exists(des_dir):
                    os.makedirs(des_dir)
                for fidx, frame in enumerate(sub_videos):
                    im = Image.fromarray(np.array(frame))
                    im.save(des_dir + '/frames_{:05d}.jpg'.format(fidx + 1))
                sub_videos = []
        print('Saved class {}'.format(i))
    with open(os.path.join(dest, '{}_videofolder.txt'.format(filename_out)),'w') as f:
        f.write('\n'.join(output))
    return


def video_creation2(dest, filename_out, dataset):
    gen = FrameGenerator()
    output = []
    for idx, value in enumerate(dataset):
        video = gen(value[0])
        label = value[1]
        output.append('%s %d %d' % ('{}/frames/{}_video_class{}_{:07d}'.format(filename_out,filename_out, label, idx), len(video), label))
        des_dir = os.path.join(dest, 'frames', '{}_video_class{}_{:07d}'.format(filename_out, label, idx))
        if not os.path.exists(des_dir):
            os.makedirs(des_dir)
        for fidx, frame in enumerate(video):
            im = Image.fromarray(np.array(frame))
            im.save(des_dir + '/frames_{:05d}.jpg'.format(fidx + 1))
        print('Generated {}/1281167'.format(idx))
    with open(os.path.join(dest, '{}_videofolder.txt'.format(filename_out)),'w') as f:
        f.write('\n'.join(output))
    return


if __name__ == '__main__':

    # Data loading code
    traindir = os.path.join(data, 'train')
    valdir = os.path.join(data, 'val')

    train_dataset = datasets.ImageFolder(traindir)
    dest = '/m100_work/IscrB_SRL4V/cugwu/data/imagenet/train/'
    file = 'train'
    video_creation2(dest, file, train_dataset)

    val_dataset = datasets.ImageFolder(valdir)
    dest = '/m100_work/IscrB_SRL4V/cugwu/data/imagenet/val/'
    file = 'val'
    video_creation2(dest, file, val_dataset)
    print('Process finished')
