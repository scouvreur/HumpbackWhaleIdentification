#!/bin/bash

kaggle competitions download -c humpback-whale-identification

mkdir data/
mv *.csv data/

unzip_images() {
	echo $1
	mkdir data/$1 && unzip $1.zip -d data/$1
	rm $1.zip
}

unzip_images train
unzip_images test

python3 scripts/subfolders.py
sh scripts/labels.sh
python3 scripts/make_validation_dir.py
