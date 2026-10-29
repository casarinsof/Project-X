# Imports
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import time

from torchvision import transforms, models
from tensorboardX import SummaryWriter
import torch
from torch import nn

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.utils import resample


# Functions
def load(f):
    return np.load(f, allow_pickle=True)['arr_0']


def plot_sample_images_data(images, labels):
    rows = 10
    columns = 10
    size = 30
    plt.figure(figsize=(size,size))
    for i in range(rows):
        imgs = images[np.where(labels == i)]
        lbls = labels[np.where(labels == i)]
        for j in range(columns):
            plt.subplot(rows,columns,i*10+j+1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(imgs[j], cmap=plt.cm.binary)
            plt.xlabel(lbls[j])
    plt.show()


def resample_data():
    x_train = load('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-train-imgs.npz')
    y_train = load('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-train-labels.npz')
    x_test = load('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-test-imgs.npz')
    y_test = load('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kkanji-test-labels.npz')

    print(f"Training Images: {x_train.shape}")
    print(f"Training Labels: {y_train.shape}")
    print(f"Test Images: {x_test.shape}")
    print(f"Training Labels: {y_test.shape}")
    print(f"Unique Kanji characters (Training): {len(np.unique(y_train))}")
    print(f"Unique Kanji characters (Test): {len(np.unique(y_test))}")

    plot_sample_images_data(x_train, y_train)

    # Reshape the 3D ndarray (69804 x 64 x 64) into a 2D array (69804 x 4096)
    new_x_train = x_train
    dim_0, dim_1, dim_2 = new_x_train.shape
    new_x_train = np.array(new_x_train).reshape(dim_0, dim_1 * dim_2)

    # Add a label column
    label = pd.DataFrame(y_train)
    new_x_train = pd.DataFrame(new_x_train)
    new_x_train['label'] = label

    # Add a count column (number of occurences of a label)
    # New shape is (69804 x 4098)
    count = pd.DataFrame(new_x_train['label'].value_counts())
    count.columns = ['count']
    count['label'] = count.index
    new_x_train = pd.merge(new_x_train, count, on='label')

    # Array for already processed labels
    my_input = []

    # Sample Size
    sample_size = 150

    # DataFrame for remaining rows
    df_rest = new_x_train.iloc[:1]

    # DataFrame for resampled rows
    df_rest_upsampled = new_x_train.iloc[:1]

    # Boolean if rows should be added to the test dataset 2
    restAdapt = False

    for item in range(len(new_x_train)):
        if (new_x_train.iloc[item, 4096] not in my_input):  # Check if the label has already been processed
            # Selction of label and DataFrame
            df_1 = new_x_train[new_x_train['label'] == new_x_train.iloc[item, 4096]]

            # Check if count bigger than sample_size, then randomly select sample size rows
            if df_1.iloc[0, 4097] > sample_size:
                testSeriesNP = df_1.index.to_numpy()  # indexes of the labels
                training, testing, _, _ = train_test_split(testSeriesNP, testSeriesNP, test_size=sample_size,
                                                           random_state=42)  # randomly select the sample_size
                df_1_upsampled = new_x_train.iloc[testing]  # randomly selected sample size
                df_rest_upsampled = new_x_train.iloc[training]  # remaining rows, used for test dataset 2
                restAdapt = True
                my_input.append(new_x_train.iloc[item, 4096])

            else:  # if count is smaller than sample_size, resample to sample_size
                df_1_upsampled = resample(df_1, random_state=42, n_samples=sample_size, replace=True)
                my_input.append(new_x_train.iloc[item, 4096])

            # Create the final DataFrame
            if item == 0:
                df_upsampled = df_1_upsampled
                df_rest = df_rest_upsampled
                restAdapt = False
            else:
                df_upsampled = pd.concat([df_1_upsampled, df_upsampled])
                if restAdapt:
                    df_rest = pd.concat([df_rest_upsampled, df_rest])
                    restAdapt = False

    # Delete
    df_upsampled.drop(['count'], axis=1, inplace=True)

    # Delete not required rows and columns
    df_rest.drop(df_rest.tail(1).index, inplace=True)
    df_rest.drop(['count'], axis=1, inplace=True)

    # Extract label
    new_y_train = df_upsampled['label']
    new_y_train = new_y_train.to_numpy().astype(int)

    # Delete column
    df_upsampled.drop(['label'], axis=1, inplace=True)

    # Dimensions
    new_dim1 = df_upsampled.shape[0]
    old_dim = 64
    # reshape into the new dimension
    new_x_train = np.array(df_upsampled).reshape(new_dim1, old_dim, old_dim)
    print(f"Training Images: {new_x_train.shape}")
    print(f"Training Labels: {new_y_train.shape}")
    print(f"Unique Kanji characters (Training): {len(np.unique(new_y_train))}")

    # Extract label
    new_y_test2 = df_rest['label']
    new_y_test2 = new_y_test2.to_numpy().astype(int)

    # Delete column
    df_rest.drop(['label'], axis=1, inplace=True)

    # concatenate test labels and new labels for the final test dataset
    final_y_test = np.concatenate([y_test, new_y_test2], -1)

    # Dimensions - original test dataset
    dim_0, dim_1, dim_2 = x_test.shape

    # Reshaping for Pandas DataFrame
    new_x_test = np.array(x_test).reshape(dim_0, dim_1 * dim_2)
    new_x_test = pd.DataFrame(new_x_test)

    # Concatenate test and rest
    final_x_test = pd.concat([new_x_test, df_rest])

    # Dimensions
    new_dim1 = final_x_test.shape[0]
    old_dim = 64

    # reshape into the new dimension for Numpy ndarray
    final_x_test = np.array(final_x_test).reshape(new_dim1, old_dim, old_dim)

    print(f"Testing Images: {final_x_test.shape}")
    print(f"Testing Labels: {final_y_test.shape}")
    print(f"Unique Kanji characters (Testing): {len(np.unique(final_y_test))}")

    np.savez_compressed('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kanji-final-train-imgs.npz', new_x_train)
    np.savez_compressed('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kanji-final-train-labels.npz', new_y_train)
    np.savez_compressed('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kanji-final-test-imgs.npz', final_x_test)
    np.savez_compressed('/m100_work/IscrB_SRL4V/cugwu/data/kanji/kanji-final-test-labels.npz', final_y_test)

    return


if __name__ == '__main__':
    resample_data()
    print('Process finished')

