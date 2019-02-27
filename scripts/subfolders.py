"""
=======================================================

 This program creates a CIFAR-like directory structure
 for the humpback whales in the training dataset.
 Run this code at the beginning of the pre-processing
 pipeline.

=======================================================
"""

print(__doc__)

import os
import pandas as pd

train = pd.read_csv("data/train.csv")
whale_id_groupby = train.groupby('Id').Image.nunique()

def create_dir_struct(groupby):
    """
    This functions takes in groupby of unique classes
    using labels in train.csv and creates
    the subdirectory structure as in CIFAR
    """
    for whale_id in groupby.index:
        print(whale_id)
        try:
            os.mkdir("data/train/" + whale_id)
        except FileExistsError:
            print("File already exists")

def mv_imgs_to_dirs(train_df):
    """
    This function takes in the train labels dataframe
    and moves corresponding images to their own
    subdirectory
    """
    for index, row in train_df.iterrows():
        src = "data/train/" + row["Image"]
        dst = "data/train/" + row["Id"] + "/" + row["Image"]
        print("source", src)
        print("dest", dst)
        os.rename(src, dst)

create_dir_struct(whale_id_groupby)
mv_imgs_to_dirs(train)
