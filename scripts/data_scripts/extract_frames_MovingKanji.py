import math
import os
import sys

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


###########################################################################################
# script to generate moving k-mnist video dataset (frame by frame) as described in
# [1] arXiv:1502.04681 - Unsupervised Learning of Video Representations Using LSTMs
#     Srivastava et al
# Modified code from:
# https://gist.github.com/praateekmahajan/b42ef0d295f528c986e2b3a0b31ec1fe?msclkid=68bf356eb00611ec860ddfaf07fbbb14
###########################################################################################


def load(f):
    return np.load(f, allow_pickle=True)['arr_0']


def generate_moving_dataset(x='./kannji_imgs', y='./kanji_labels', dest='./', flag='train', frame_size=(224, 224),
                            num_frames=30, original_size=64, nums_per_image=1):
    """
        Args:
        x: String, path for loading the data of the training/test set.
        y: String, path for loading the labels of the training/test set.
        dest: destination where to save the image
        flag: Flag to say we are generating training or test videos.
        shape: Shape we want for our moving images (new_width and new_height)
        num_frames: Number of frames in a particular movement/animation/gif
        original_size: Real size of the images (eg: MNIST is 28x28, Kanji is 64x64)
        nums_per_image: Digits per movement/animation/gif.
    """
    kanji_data = load(x)
    kanji_labels = load(y)
    width, height = frame_size
    output = []

    # Get how many pixels can we move around a single image
    lims = (x_lim, y_lim) = width - original_size, height - original_size

    for idx in range(len(kanji_data)):
        # Randomly generate direction, speed and velocity for both images
        direc = np.pi * (np.random.rand(1) * 2 - 1)
        speed = np.random.randint(5, size=1) + 2
        veloc = np.asarray([float(speed * math.cos(direc)), float(speed * math.sin(direc))])

        image = Image.fromarray(kanji_data[idx]).resize((original_size, original_size))
        label = kanji_labels[idx]
        output.append('%s %d %d' % ('{}/frames/{}_video_class{}_{:05d}'.format(flag, flag, label, idx),
                                    int(num_frames), label))
        des_dir = os.path.join(dest, 'frames', '{}_video_class{}_{:05d}'.format(flag, label, idx))
        if not os.path.exists(des_dir):
            os.makedirs(des_dir)

        # Generate tuples of (x,y) i.e initial positions for the image
        pos = np.asarray((np.random.rand() * x_lim, np.random.rand() * y_lim))

        # Generate new frames for num_frames times
        for frame_idx in range(num_frames):

            frame = Image.new('L', (width, height))
            frame.paste(image, tuple(pos.astype(int)))

            # Update positions based on velocity
            next_pos = pos + veloc
            # bounce off wall if we hit one
            for j, coord in enumerate(next_pos):
                if coord < -2 or coord > lims[j]+2:
                    veloc = tuple(list(veloc[:j]) + [-1 * veloc[j]] + list(veloc[j+1:]))

            pos = pos + veloc

            frame.save(des_dir + '/frames_{:05d}.jpg'.format(frame_idx + 1))
    with open(os.path.join(dest, '{}_videofolder.txt'.format(flag)), 'w') as f:
        f.write('\n'.join(output))
    return


# def generate_moving_dataset_v2(x='./kannji_imgs', y='./kanji_labels', dest='./', flag='train', frame_size=(224, 224),
#                             num_frames=30, original_size=64, nums_per_image=2):
#     '''
#     Args:
#         Args:
#         x: String, path for loading the data of the training/test set.
#         y: String, path for loading the labels of the training/test set.
#         dest: destination where to save the image
#         flag: Flag to say we are generating training or test videos.
#         shape: Shape we want for our moving images (new_width and new_height)
#         num_frames: Number of frames in a particular movement/animation/gif
#         original_size: Real size of the images (eg: MNIST is 28x28, Kanji is 64x64)
#         nums_per_image: Digits per movement/animation/gif.
#
#     '''
#     kanji_data = load(x)
#     kanji_labels = load(y)
#     width, height = frame_size
#     output = []
#
#     # Get how many pixels can we move around a single image
#     lims = (x_lim, y_lim) = width - original_size, height - original_size
#
#     for idx in range(len(kanji_data)):
#         # Randomly generate direction, speed and velocity for both images
#         direcs = np.pi * (np.random.rand(nums_per_image) * 2 - 1)
#         speeds = np.random.randint(5, size=nums_per_image) + 2
#         veloc = np.asarray([(float(speed * math.cos(direc)), float(speed * math.sin(direc))) for direc, speed in zip(direcs, speeds)])
#
#         image = Image.fromarray(kanji_data[idx]).resize((original_size, original_size))
#         label = kanji_labels[idx]
#         output.append('%s %d %d' % ('{}/frames/{}_video_class{}_{:05d}'.format(flag, flag, label, idx),
#                                     int(num_frames), label))
#         des_dir = os.path.join(dest, 'frames', '{}_video_class{}_{:05d}'.format(flag, label, idx))
#         if not os.path.exists(des_dir):
#             os.makedirs(des_dir)
#
#         # Get a list containing PIL images randomly sampled from the database
#         others_images = [Image.fromarray(kanji_data[r]).resize(original_size, original_size)
#                          for r in np.random.randint(0, len(kanji_data)-1, (nums_per_image-1))]
#
#         images = [image].extend(others_images)
#         # Generate tuples of (x,y) i.e initial positions for nums_per_image (default : 2)
#         positions = np.asarray([(np.random.rand() * x_lim, np.random.rand() * y_lim) for _ in range(nums_per_image)])
#
#         # Generate new frames for the entire num_framesgth
#         for frame_idx in range(num_frames):
#
#             canvases = [Image.new('L', (width, height)) for _ in range(nums_per_image)]
#             canvas = np.zeros((1, width, height), dtype=np.float32)
#
#             # In canv (i.e Image object) place the image at the respective positions
#             # Super impose both images on the canvas (i.e empty np array)
#             for i, canv in enumerate(canvases):
#                 canv.paste(images[i], tuple(positions[i].astype(int)))
#                 canvas += canv
#
#             # Get the next position by adding velocity
#             next_pos = positions + veloc
#
#             # Iterate over velocity and see if we hit the wall
#             # If we do then change the  (change direction)
#             for i, pos in enumerate(next_pos):
#                 for j, coord in enumerate(pos):
#                     if coord < -2 or coord > lims[j] + 2:
#                         veloc[i] = list(list(veloc[i][:j]) + [-1 * veloc[i][j]] + list(veloc[i][j + 1:]))
#
#             # Make the permanent change to position by adding updated velocity
#             positions = positions + veloc
#             Image.fromarray(canvas).save(des_dir + '/frames_{:05d}.jpg'.format(frame_idx + 1))
#     with open(os.path.join(dest, '{}_videofolder.txt'.format(flag)), 'w') as f:
#         f.write('\n'.join(output))
#     return


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Command line options')
    parser.add_argument('--x', type=str, dest='x', default='/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-test-imgs.npz',
                        help='Path to the samples saved as .npz file.')
    parser.add_argument('--y', type=str, dest='y', default='/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-test-labels.npz',
                        help='Path to the labels saved as .npz file.')
    parser.add_argument('--dest', type=str, dest='dest', default='/m100_work/IscrB_SRL4V/cugwu/data/movingkanji/val/',
                        help='Path to where the training or test videos will be saved.')
    parser.add_argument('--flag', type=str, dest='flag', default='val', help='Flag to distinguish between training or test set')
    parser.add_argument('--frame_size', type=int, dest='frame_size', default=(224, 224))
    parser.add_argument('--num_frames', type=int, dest='num_frames', default=30)
    parser.add_argument('--original_size', type=int, dest='original_size', default=64)
    parser.add_argument('--nums_per_image', type=int, dest='nums_per_image', default=1)  # number of digits in each frame
    args = parser.parse_args(sys.argv[1:])

    # Create a dictionary of key,values and giv it in input to the function
    generate_moving_dataset(**{k: v for (k, v) in vars(args).items() if v is not None})

    # if args.nums_per_image > 1:
    #     generate_moving_dataset_v2(**{k: v for (k, v) in vars(args).items() if v is not None})
    # else:
    #     generate_moving_dataset(**{k: v for (k, v) in vars(args).items() if v is not None})

    print('Processed Finished')
