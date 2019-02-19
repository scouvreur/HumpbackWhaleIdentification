import pandas as pd
import os
from shutil import copyfile

train = pd.read_csv("train.csv")
whale_id_groupby = train.groupby('Id').Image.nunique()

def create_dir_struct(groupby):
	"""
	This functions takes in groupby of unique classes
	using labels in train.csv and creates
	the subdirectory structure as in CIFAR
	"""
	os.mkdir("train2")
	os.chdir("train2")
	# Create directory structure
	for whale_id in groupby.index:
		print(whale_id)
		try:
			os.mkdir(whale_id)
		except FileExistsError:
			print("File already exists")
	return None

def mv_imgs_to_dirs(train_df):
	"""
	This function takes in the train labels dataframe
	and moves corresponding images to their own
	subdirectory
	"""
	for index, row in train_df.iterrows():
		src = "../train/" + row["Image"]
		dst = row["Id"] + "/" + row["Image"]
		print("source",src)
		print("dest",dst)
		copyfile(src, dst)
	return None

create_dir_struct(whale_id_groupby)
mv_imgs_to_dirs(train)
