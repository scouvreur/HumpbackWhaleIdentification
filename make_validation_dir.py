"""
=======================================================

 This program samples whales from the training set
 with more than k samples, and takes a random sample
 of them and places them into the validation folder.
 Run this code at the beginning of the pre-processing
 pipeline.

=======================================================
"""

print(__doc__)

import os

train_path = 'data/train/'
validation_path = 'data/validation/'

try:
    os.mkdir(validation_path)
except FileExistsError:
    print("Folder already exists")

def list_val_dirs(n_samples, train_path):
    """Get directories for validation set with
    more than k samples.

    Args:
        n_samples (list): the list of validation dirs.
        val_sample_split (float): percentage of images
        to move to validation set.
    Returns:
        list of validation dirs.
    Raises:
        Exception: if n_samples is negative.
    """
    if n_samples <= 5:
        raise Exception('Please enter a number of samples > 5')
    train_dirs = os.listdir(train_path)
    val_dirs = []
    for whale in train_dirs:
        if len(os.listdir(train_path + whale)) > int(n_samples):
            val_dirs.append(whale)
    return val_dirs

val_dirs = list_val_dirs(n_samples=5, train_path=train_path)

def move_samples(val_dirs, val_sample_split):
    """Move validation samples to individual dirs.

    Args:
        val_dirs (list): the list of validation dirs.
        val_sample_split (float): percentage of images
        to move to validation set.
    Returns:
        None
    Raises:
        FileExistsError: if whale dir already exists in
        the validation dir.
    """
    for whale in val_dirs:
        try:
            os.mkdir(validation_path + whale)
        except FileExistsError:
            print("Folder already exists")
        items = os.listdir(train_path + whale)
        to_move = items[0:int(val_sample_split * len(items))]
        for item in to_move:
            print(whale,item)
            src = train_path + whale + "/" + item
            dst = validation_path + whale + "/" + item
            os.rename(src, dst)

move_samples(val_dirs=val_dirs, val_sample_split=0.2)
