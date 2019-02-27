#!/bin/bash

kaggle competitions download -c humpback-whale-identification

mkdir data
mkdir data/train/
mkdir data/test/

mv sample_submission.csv data/
mv train.csv data/

unzip_images() {
	echo $1
	mv $1.zip data/$1/$1.zip
	cd data/$1/
	unzip $1.zip
	rm $1.zip
	cd ../../
}

unzip_images train
unzip_images test
